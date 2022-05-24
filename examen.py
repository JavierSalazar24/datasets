import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('datasets/train.csv')


# Previsualiación
print(df.head())


# Dimensión del df
print(df.shape)

# Conocer la cantidad de datos faltantes por cada columna
print(df.isnull().sum())

# Tipo de datos en general
print(df.dtypes)

# Tipo de datos por columna
for column in df:
    print(df[column].dtypes)

# Obtener más info de la base de datos
print(df.info())

# Describir base de datos
print(df.describe())

# Conocer si hay datos duplicados
print(df.duplicated().sum())

# Obtener los nombres de las columnas en una lista e Iterar sobre la lista para conocer campos nulos
col_names = df.columns.tolist()
for column in col_names:
    print("Valores nulos en <" + column +
          ">: " + str(df[column].isnull().sum()))

# Cambiar un diccionario con los valores originales por valores de reemplazo de columna sex
d = {'male': 'M', 'female': 'F'}
df['Sex'] = df['Sex'].apply(lambda x: d[x])
# Checar el cambio
print(df['Sex'].head())

# Crear cruce de tabla o de información
ct = pd.crosstab(df['Survived'], df['Sex']).plot(kind='bar')

# Agrupar por pclass y gender la suma de los sobrevivientes(survived)
pclass_survived = df.groupby(['Pclass', 'Sex'])['Survived'].sum()
print(pclass_survived)

# count de sobrevivientes y renderizarlo en tipo bar
# Crear una figura de 15x15
plt.figure(figsize=(15, 15))

# Generar 2 columnas para renderizar varias gráficas
plt.subplot2grid((2, 3), (0, 0))

# Count de sobrevivientes y renderizarlo en tipo barra
t = df['Survived'].value_counts().plot(kind='bar')
plt.title('Sobrevivieron - Cuenta total')
plt.xlabel('Sobrevivió')
plt.ylabel('Cantidad de Sobrevivientes')

for barra in t.containers:
    t.bar_label(barra, label_type='edge')

plt.show()
