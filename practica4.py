import pandas as pd
import matplotlib.pyplot as plt

#crear tablas sencillas con count
df = pd.read_csv('users_modify.csv')

#selecciona solamente las columnas gender y role
df = df[['gender','role']]
# print(df.head())

df['gender'].value_counts().plot(kind = 'pie')
plt.show()

df['role'].value_counts().plot(kind = 'barh')
plt.show()


df.plot(kind='scatter',x = 'first_name', y = 'car' )
plt.show()

