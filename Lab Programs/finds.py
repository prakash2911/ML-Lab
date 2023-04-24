import pandas as pd
df = pd.read_excel("findsdata2.xlsx")
data = df.values
column_head = df.columns
h = data[0]
len = h.size
for x in data:
    if x[len-1] == 'YES':
        for i in range(len-1):
            if h[i] != x[i]:
                h[i] = '?'
for i in range(len):
    print((column_head[i] + '\t' + h[i]).expandtabs(26))