from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

data = [[-1, 2], [-0.5, 6], [0, 10], [1, 18]]
print("Data before preprocessing: ", *data, sep='\n')
scaler = MinMaxScaler()
scaler.fit(data)
data = scaler.transform(data)
print("\nData after preprocessing: ", *data, sep='\n')

plt.bar([data[i][0] for i in range(len(data))], [data[i][1] for i in range(len(data))], width=0.5)
plt.plot()
plt.show()