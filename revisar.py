from matplotlib import colors
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('datasets/datasets/sector_minero.csv', encoding="ISO-8859-1")

# df.drop_columns('trimestre')

# cantidad de datos = 1266
# print(df.duplicated().sum())

# 1
# Cambiar un dato por otro
# df['Genero'] = df['Genero'].replace('No informa','Desconocido')
df['Area'] = df['Area'].replace(
    'Combustibles-ProducciÃ³n', 'Combustibles-Produccion')

# 2
# Eliminar duplicados
#df.drop_duplicates(subset=['Area', 'Genero','Cantidad_Empleados','Salario_Promedio'])

# 3
# # Mostrar el salario promedio que gana un trabajador en cada area, independientemente del genero.
# salario_promedio = df.groupby(['Area']).agg(
#     {'Salario_Promedio': 'mean'}).reset_index()

# # Imprimir las cantodades
# print(salario_promedio)

# # Imprimir las cantidades pero con 2 cifras después del punto (Estas cifras se redondean al numero mayor)
# print(round(salario_promedio, 2))

# # Graficar las cantidades
# salario_promedio.plot(kind='bar', x='Area', y='Salario_Promedio',
#                       title='Salario promedio que gana un trabajador en cada área')

# # Hacer que se pongan las cantidades arriba de su barra correspondiente
# for i in range(len(salario_promedio['Area'])):
#     plt.text(i, salario_promedio['Salario_Promedio'][i],
#              round(salario_promedio['Salario_Promedio'][i], 2), ha='center')


# 4
# Mostrar un círculo con los empleados que trabajan en una área en específico, o ...
# colores = ['#712B75', '#E6AF2E', '#6E6D6D','#8E3200','#22577E','#4E944F','#614124','#F76E11','#F55353']
# df['Area'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=colores)
# plt.ylabel("")
# plt.rcParams['toolbar'] = 'None'


# 5
# ...cantidad de generos que trabajan en una área(no importa si es la misma línea y se tenga que cambiar el dato) || Está respuesta viene en el coódigo de abajo.

# Mostrar que cantidad de hombres y de mujeres trabajan en minería cualquier área

# colores = ['#383838', '#40DFEF', '#E78EA9']
# plt.rcParams['toolbar'] = 'None'
# ct = pd.crosstab(df['Area'], df['Genero']).plot(kind='bar', color=colores)
# plt.xlabel("Area")
# plt.ylabel("Genero")

# for barra in ct.containers:
#     ct.bar_label(barra, label_type='edge') #ascending=True)


# 6
# colores = ['#383838', '#40DFEF', '#E78EA9']
# ct = pd.crosstab(df['Area'], df['Salario_Promedio']).plot(kind='bar', color=colores, ascending=True)
# plt.xlabel("Genero")
# plt.ylabel("Salario_Promedio")
# plt.legend(loc="lower right")

# for barra in ct.containers:
#     ct.bar_label(barra, label_type='edge')


# 7
# Saber cuantos trabajadores totales hay en cada area, en barra
# colores = ['#08e778']
# t = df['Area'].value_counts().plot(kind='bar', color=colores)
# for barra in t.containers:
#      t.bar_label(barra, label_type='edge')


# 'best (la mejor posición según python)', 'upper right (arriba a la derecha)', 'upper left (arriba a la izquierda)', 'lower left (abajo a la izquierda)', 'lower right (abajo a la derecha)', 'right (derecha)', 'center left (centrado a la izquierda)', 'center right (centrado a la derecha)', 'lower center (centrado abajo)', 'upper center (centrado arriba)', 'center (centrado)'

# 8
# group = df.groupby(["Genero", "Area"])
# print(group.size().reset_index(name='Cantidad de empleados'))


# Mostrar graficas
plt.show()

# df.to_csv('sector_minero_copia.csv',index=False)
