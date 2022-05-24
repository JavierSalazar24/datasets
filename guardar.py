import pandas as pd
import matplotlib.pyplot as plt

#agregar el csv al dataframe
df = pd.read_csv('usuarios_completo.csv')

#selecciona  columnas para analisis
df = df[['gender','favorite_app']]
#print(df.head())

#agrupar gender y favorite_app del dataframe
group=df.groupby(["gender","favorite_app"])
# print(group)

print(group.size().reset_index(name='counts'))

df['favorite_app'].value_counts().plot(kind = 'pie')
plt.show()
