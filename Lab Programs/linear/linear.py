import pandas as pd
data = pd.read_excel("linear.xlsx").values.tolist()
pro_d = [[x[0], x[1], x[2], x[0]**2, x[1]**2, x[0]*x[1], x[0]*x[2], x[1]*x[2]] for x in data]
sum_d = [sum(x) for x in zip(*pro_d)]
n = len(data)
sum_x1x1 = sum_d[3] - (sum_d[0] ** 2) / n
sum_x2x2 = sum_d[4] - (sum_d[1] ** 2) / n
sum_x1y = sum_d[6] - (sum_d[0] * sum_d[2]) / n
sum_x2y = sum_d[7] - (sum_d[1] * sum_d[2]) / n
sum_x1x2 = sum_d[5] - (sum_d[0] * sum_d[1]) / n
denom = (sum_x1x1 * sum_x2x2) - (sum_x1x2 ** 2)
b1 = ((sum_x2x2 * sum_x1y) - (sum_x1x2 * sum_x2y)) / denom
b2 = ((sum_x1x1 * sum_x2y) - (sum_x1x2 * sum_x1y)) / denom
a = (sum_d[2]/n) - b1*(sum_d[0]/n) - b2*(sum_d[1]/n)
x1, x2 = int(input("Enter the value of x1: ")), int(input("Enter the value of x2: "))
print("The value of y: ", (a + b1*x1 + b2*x2))