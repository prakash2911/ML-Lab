import pandas as pd
import numpy as np
df = pd.read_excel("candidate.xlsx")
data = df.values
column_head = df.columns
specific_h = data[0]
len = specific_h.size
specific_h = np.delete(specific_h, len-1, axis=0)
general_h = []
for x in data:
    if x[len-1] == 'YES':
        for i in range(len-1):
            if specific_h[i] != x[i]:
                temp = ('?,'*i + str(specific_h[i]) + ',?'*(len-i-2)).split(',')
                if temp in general_h:
                    general_h.remove(temp)
                specific_h[i] = '?'
    elif x[len-1] == 'NO':
        for i in range(len-1):
            if x[i] != specific_h[i]:
                temp = ('?,'*i + str(specific_h[i]) + ',?'*(len-i-2)).split(',')
                general_h.append(temp)
print('Specific Hypothesis: ', specific_h, '\nGeneral Hypothesis: ', *general_h, sep='\n')