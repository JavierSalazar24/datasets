import pandas as pd
import matplotlib.pyplot as plt

#crosstab
#Agregar el archivo para analisis con pandas
df = pd.read_csv('usuarios_completo.csv')
#Seleccionar las columnas a procesar
df = df[['gender','favorite_app']]
#Crear un cruce entre columnas y filas
ct = pd.crosstab(df['gender'],df['favorite_app']).plot(kind='bar')
plt.title('Grafica para cruce de genero y app favorita')
# x = plt.subplot()
# x.set_xlabel('Genero')
# x.set_ylabel('Cantidad de roles')
plt.xlabel("Genero")
plt.ylabel("App favoritas")

for barra in ct.containers:
    ct.bar_label(barra, label_type='edge')
plt.savefig("grafica.png")
plt.show()
