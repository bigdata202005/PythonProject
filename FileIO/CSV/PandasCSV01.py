import pandas as pd
data = pd.read_csv("./data.csv", header=None)
print(type(data))
print(data)
#         [열][행]
print(data[0][0])
print(data[1][0])
print(data[2][0])
print(data[3][0])
print("-" * 80)
for i in data:
    print("{}. {}".format(data[0][i], data[1][i]))
print("-" * 80)

data = pd.read_csv("./data.tsv", delimiter='\t', header=None)
print(type(data))
print(data)
