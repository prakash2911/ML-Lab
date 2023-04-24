import pandas as pd
df = pd.read_csv("listtheneliminate.csv")
data = df.values
column_head = df.columns
col_len = data[0].size
vs = []
possible_values = [list(df[column].unique()) + ['?'] for column in df.columns[:-1]]
def gen_h(i, x):
    if i == col_len-1:
        vs.append(x.copy())
    else:
        for j in range(len(possible_values[i])):
            x[i] = possible_values[i][j]
            gen_h(i+1, x)
gen_h(0, ['?' for i in range(col_len-1)])
final_h = []
for h in vs:
    flag = 0
    for x in data:
        if flag == 1:
            break
        if x[col_len-1] == 'YES':
            for i in range(col_len-1):
                if not(h[i] == x[i] or h[i] == '?'):
                    flag = 1
                    break
    if flag == 0:
        final_h.append(h)
for h in final_h:
    flag = 0
    for x in data:
        if x[col_len-1] == 'NO':
            for i in range(col_len-1):
                if h[i] == x[i] and h[i] != '?':
                    flag += 1
    if flag == (col_len - h.count('?') - 1):
        final_h.remove(h)
print("All possible consistent hypothesis: \n",*final_h, sep='\n')