import pandas as pd

# df = pd.read_csv('datasets/datasets/sector_minero.csv')
df = pd.read_csv('datasets/sector_minero.csv', encoding="ISO-8859-1")


df['Area'] = df['Area'].replace(
    'Litio-exploración y financiación', 'Litio-exploracion y financiacion')
df['Area'] = df['Area'].replace(
    'Metaliferos-exploración y financiación', 'Metaliferos-exploracion y financiacion')
df['Area'] = df['Area'].replace('Rocas de aplicación', 'Rocas de aplicacion')
