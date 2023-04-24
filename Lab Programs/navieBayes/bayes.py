import pandas as pd

df = pd.read_excel(r'buy_car.xlsx')
n = df.value_counts(df['Buys_Car'] == 'Yes')
pyes = n[1] / (n[0] + n[1])
pno = n[0] / (n[0] + n[1])


def predict():
    global pyes, pno
    fields = {}
    for i in ['Age', 'Income', 'Marital_Status', 'Cred_rating']:
        fields[i] = input("Enter " + i + ": ")
    for i in fields:
        pyes *= (df.value_counts((df[i] == fields[i]) & (df['Buys_Car'] == 'Yes'))[1]) / n[1]
        pno *= (df.value_counts((df[i] == fields[i]) & (df['Buys_Car'] == 'No'))[1]) / n[0]
    print("\nProbability of yes: ", pyes, "\nProbability of no: ", pno, "\n\nBuys Car: No")


predict()
