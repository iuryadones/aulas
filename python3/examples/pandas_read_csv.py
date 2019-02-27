import pandas as pd

ler_csv = pd.read_csv('base.csv', sep=';')

print(ler_csv)

X = ler_csv[['A','B']]
y = ler_csv['y']

print('Features', X)
print('Label', y)
