import pandas as pd

df = pd.read_csv('datasets/banco.csv')


print('Dimensión: ', df.ndim)

print('Datos nulos: ', df.isnull())

print('Tipo de datos en general: ', df.dtypes)

for column in df:
    print('Tipo de datos por culuma: ', df[column].dtypes)

print('Uso de .info', df.info())

print('Uso de .describe', df.describe())

print('Datos duplicados: ', df.duplicated().sum())
