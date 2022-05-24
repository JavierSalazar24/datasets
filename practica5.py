import pandas as pd
import matplotlib.pyplot as plt

# #crear tablas sencillas con count
df = pd.read_csv('usuarios_completo.csv')

# selecciona solamente las columnas gender y role
df = df[['company', 'car']]
# print(df.head())

df['company'].value_counts().plot(kind='pie')
plt.show()

df['car'].value_counts().plot(kind='barh')
plt.show()
