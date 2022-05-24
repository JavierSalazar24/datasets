import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('publicidad.csv', encoding="ISO-8859-1")

# Mostrar dataset
# print(df.head(8))

# Contar duplicados
# print(df.duplicated().sum())

# Eliminar duplicados
# print(df.drop_duplicates(subset=['pais', 'edad', 'porcentaje']))

# Imprimir los nulos del dataframe
# print(df.isnull())

# Rellenar datos nulos.
df['pais'] = df['pais'].fillna('Espania')
df['edad'] = df['edad'].fillna('>74')

# Cambiar un dato por otro
df['pais'] = df['pais'].replace('EspaÃ±a', 'Espania')
# print(df.head(8))

# Mostrar el promedio final de las personas que miraron publicidad
# promedio = df['porcentaje'].mean()
# print(f'Promedio final de las personas que miraron publicidad:\n{promedio}%')

# Mostrar la edad máxima de las personas que miraron publicidad
# edad_maxima = df['edad'].max()
# print(
#     f'Edad máxima de las personas que miraron publicidad:\n{edad_maxima} años')

# Mostrar la edad minima de las personas que miraron publicidad
# edad_minima = df['edad'].min()
# print(f'Edad mínima de las personas que miraron publicidad:\n{edad_minima} años')

# Grafica final sin ordenar
# group = df.groupby(["edad", "porcentaje"]).size().reset_index()
# t = group.plot(x='edad', y='porcentaje', kind='bar')

# for barra in t.containers:
#     t.bar_label(barra, label_type='edge')

# Grafica final ordenada
# df = df.sort_values('porcentaje', ascending=True)
# plt.bar(df['edad'], df['porcentaje'])

# for i in range(len(df['porcentaje'])):
#     plt.text(df['edad'][i], df['porcentaje'][i],
#              str(df['porcentaje'][i])+'%', ha='center')

# Gráfica pie
# plt.pie(df['porcentaje'], labels=df['edad']+' años', autopct='%1.1f%%')
fig, ax = plt.subplots()

edad_mitad = df[(df['edad'] >= '14-19') & (df['edad'] <= '35-44')
                ].assign(edad_limite='14 a 44 años')
# porcentaje_final = edad_mitad.groupby(['edad_limite']).agg(
#     {'porcentaje': 'max'}).reset_index()
# re = plt.bar(porcentaje_final['edad_limite'],
#              porcentaje_final['porcentaje'], label='Porcentajes')

# ax.bar_label(re, padding=3)

edad_mitad2 = df[(df['edad'] >= '45-54') & (df['edad'] <= '>74')
                 ].assign(edad_limite='45 a mayor de 74 años')
porcentaje_final2 = edad_mitad2.groupby(['edad_limite']).agg(
    {'porcentaje': 'max'}).reset_index()

re = plt.bar(porcentaje_final2['edad_limite'],
             porcentaje_final2['porcentaje'], label='Porcentajes', color=["#83BD75"])

ax.bar_label(re, padding=3)

# grupo1 = edad_mitad.groupby(["edad_limite", "porcentaje"])
# porcentaje_final = edad_mitad.groupby(['edad_limite']).agg(
#     {'porcentaje': 'min'}).reset_index()

# grupo2 = edad_mitad2.groupby(["edad_limite", "porcentaje"])


# grupos = pd.concat([porcentaje_final, porcentaje_final2])
# grupos = grupos.reset_index()

# re = plt.bar(porcentaje_final['edad_limite'], porcentaje_final['porcentaje'],
#              label='Porcentajes')

# ax.set_xticks(porcentaje_final['edad_limite'])


# plt.title('Porcentaje de individuos que vio publicidad')
# plt.axis("equal")
# plt.legend(['porcentaje de edad de 14 a 44 años'])
plt.xlabel("Edades")
plt.ylabel("Porcentaje")

# plt.savefig("grafica_ordenada.png")
plt.show()

# df.to_csv('publicidad_completo.csv', index=False)
