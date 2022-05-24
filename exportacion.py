import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('exportacion_importacion_minera.csv', encoding="ISO-8859-1")

# Es de aquí....
# Agrupar y graficar por país de exportación en dolares de exportación
exportacion = df.groupby(
    ["Pais_exportacion", "Exportacion_dolares"]).size().reset_index()
e = exportacion.plot(x='Pais_exportacion', y='Exportacion_dolares', kind='bar')
# Poner cantidades arriba de la barra
for barra in e.containers:
    e.bar_label(barra, label_type='edge')
# ...hasta aquí

# Obtener la cantidad maxima de dolares en exportacion
exportacion_maxima = df['Exportacion_dolares'].max()
# El signo de gato es para que aparezca el signo de pesos al lado de la cantidad, no por otra cosa
print(
    f"Cantidad máxima en millones de dolares en exportación: ${exportacion_maxima}")
# Obtener la cantidad minima de dolares en exportacion
exportacion_minima = df['Exportacion_dolares'].min()
# El signo de gato es para que aparezca el signo de pesos al lado de la cantidad, no por otra cosa
print(
    f"Cantidad minima en millones de dolares en exportación: ${exportacion_minima}")
# Obtener el promedio de dolares en exportacion
promedio_exportacion = df['Exportacion_dolares'].mean()
# El signo de gato es para que aparezca el signo de pesos al lado de la cantidad, no por otra cosa
print(
    f"Cantidad promedio en millones de dolares en exportación: ${promedio_exportacion}")

#

# Es de aquí....
# Agrupar y graficar por país de importacion en dolares de importacion
importacion = df.groupby(
    ["Pais_importacion", "Importacion_dolares"]).size().reset_index()
e = importacion.plot(x='Pais_importacion', y='Importacion_dolares', kind='bar')
# Poner cantidades arriba de la barra
for barra in e.containers:
    e.bar_label(barra, label_type='edge')
# ...hasta aquí

# Obtener la cantidad maxima de dolares en importacion
importacion_maxima = df['Importacion_dolares'].max()
# El signo de gato es para que aparezca el signo de pesos al lado de la cantidad, no por otra cosa
print(
    f"Cantidad máxima en millones de dolares en importacion: ${importacion_maxima}")
# Obtener la cantidad minima de dolares en importacion
importacion_minima = df['Importacion_dolares'].min()
# El signo de gato es para que aparezca el signo de pesos al lado de la cantidad, no por otra cosa
print(
    f"Cantidad minima en millones de dolares en importacion: ${importacion_minima}")
# Obtener el promedio de dolares en importacion
promedio_importacion = df['Importacion_dolares'].mean()
# El signo de gato es para que aparezca el signo de pesos al lado de la cantidad, no por otra cosa
print(
    f"Cantidad promedio en millones de dolares en exportación: ${promedio_importacion}")

plt.show()
