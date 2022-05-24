import pandas as pd
import matplotlib.pyplot as plt

# Empezar a leer el archivo csv
df = pd.read_csv('user_data.csv')

# Imprimir los nulos del dataframe
print(df.isnull())

# Rellenar las filas nulas de la columna lenguage
df['language'] = df['language'].fillna('Other')

# Guardar una copia con las columnas modificadas
df.to_csv('user_modify.csv', index =  False)



