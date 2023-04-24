import pandas as pd
import math

df = pd.read_excel("id3.xlsx")
column_head = list(df.columns)


def eval_entropy(positive_num, negative_num):
    if positive_num == 0 or negative_num == 0:
        return 0
    elif positive_num == negative_num:
        return 1
    else:
        total_num = positive_num + negative_num
        return -((positive_num / total_num) * math.log2(positive_num / total_num)) - (
                (negative_num / total_num) * math.log2(negative_num / total_num))


def calc_entropy(col_head, data_frame, values):
    for column_name in values:
        if column_name == 'Entropy':
            continue
        values[column_name]['Gain'] = values['Entropy']
        for value_name in values[column_name]['Values']:
            positive_num = \
                data_frame[(data_frame[column_name] == value_name) & (data_frame[col_head[-1]] == 'YES')].shape[0]
            negative_num = \
                data_frame[(data_frame[column_name] == value_name) & (data_frame[col_head[-1]] == 'NO')].shape[0]
            entropy = eval_entropy(positive_num, negative_num)
            values[column_name]['Values'][value_name] = entropy
            values[column_name]['Gain'] = values[column_name]['Gain'] - (
                    ((positive_num + negative_num) / data_frame.shape[0]) * entropy)
    return values


def gen_possible_values(col_head, data_frame):
    values = {}
    for i in range(len(col_head) - 1):
        unique_value_array = list(data_frame[col_head[i]].unique())
        unique_value_dict = {'Values': {}}
        for x in unique_value_array:
            unique_value_dict['Values'].setdefault(x, 0)
        unique_value_dict.setdefault('Gain', 0)
        values.setdefault(col_head[i], unique_value_dict)
    entropy = eval_entropy(data_frame[data_frame[col_head[-1]] == 'YES'].shape[0], data_frame[data_frame[col_head[-1]] == 'NO'].shape[0])
    values.setdefault('Entropy', entropy)
    values = calc_entropy(col_head, data_frame, values)
    return values


def gen_id3(col_head, data_frame):
    values = gen_possible_values(col_head, data_frame)
    max_gain_column_name = col_head[0]
    for column_name in values:
        if column_name == 'Entropy':
            continue
        if values[column_name]['Gain'] > values[max_gain_column_name]['Gain']:
            max_gain_column_name = column_name
    id3 = {}
    sub_id3 = {}
    for value_name in list(values[max_gain_column_name]['Values'].keys()):
        if values[max_gain_column_name]['Values'][value_name] == 0:
            if (
                    data_frame[
                        (data_frame[max_gain_column_name] == value_name) & (data_frame[col_head[-1]] == 'YES')].shape[
                        0]) == 0:
                sub_id3.setdefault(value_name, 'NO')
            else:
                sub_id3.setdefault(value_name, 'YES')
        else:
            col_head_copy = col_head.copy()
            col_head_copy.remove(max_gain_column_name)
            sub_id3.setdefault(value_name, gen_id3(col_head_copy,
                                                   data_frame[data_frame[max_gain_column_name] == value_name].drop(
                                                       max_gain_column_name, axis=1).drop_duplicates()))
    id3.setdefault(max_gain_column_name, sub_id3)
    return id3


possible_values = gen_id3(column_head, df)
print(possible_values)
