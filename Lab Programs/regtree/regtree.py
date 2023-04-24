import pandas as pd
import numpy as np

class Node:
    def __init__(self, label=None, feature=None, threshold=None, left=None, right=None):
        self.label = label
        self.feature = feature
        self.threshold = threshold
        self.left = left
        self.right = right

def regression_tree(data, target_attr, attrs):
    
    if len(np.unique(data[target_attr])) == 1:
        return Node(label=data[target_attr].iloc[0])

    if len(attrs) == 0:
        return Node(label=data[target_attr].mean())

    best_feature, best_threshold, best_mse = None, None, None

    for attr in attrs:
        for threshold in np.unique(data[attr])[:-1]:
            left_data = data[data[attr] <= threshold]
            right_data = data[data[attr] > threshold]
            mse = calc_mse(left_data[target_attr], right_data[target_attr])
            if best_mse is None or mse < best_mse:
                best_feature, best_threshold, best_mse = attr, threshold, mse

    left_data = data[data[best_feature] <= best_threshold]
    right_data = data[data[best_feature] > best_threshold]

    left_node = regression_tree(left_data, target_attr, [attr for attr in attrs if attr != best_feature])
    right_node = regression_tree(right_data, target_attr, [attr for attr in attrs if attr != best_feature])

    return Node(feature=best_feature, threshold=best_threshold, left=left_node, right=right_node)


def calc_mse(left_data, right_data):
    n = len(left_data) + len(right_data)
    left_weight = len(left_data) / n
    right_weight = len(right_data) / n
    left_mean = left_data.mean()
    right_mean = right_data.mean()
    return left_weight * ((left_data - left_mean) ** 2).sum() + right_weight * ((right_data - right_mean) ** 2).sum()


def print_tree(node, depth=0):
    prefix = "  " * depth
    if node.label is not None:
        print(f"{prefix}--> {node.label:.2f}")
    elif node.feature is not None:
        print(f"{prefix}{node.feature} <= {node.threshold}")
        print_tree(node.left, depth + 1)
        print_tree(node.right, depth + 1)


data = pd.read_excel("hours_study.xlsx")
target_attr = "Grade"
attrs = [attr for attr in data.columns if attr != target_attr]
tree = regression_tree(data, target_attr, attrs)
print_tree(tree)
