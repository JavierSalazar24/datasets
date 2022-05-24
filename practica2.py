import pandas as pd

df = pd.read_csv('datasets/usuarios_incompleto.csv')

df['company'] = df['company'].fillna('Other')
df['car'] = df['car'].fillna('Company')
df['favorite_app'] = df['favorite_app'].fillna('WhatsApp')
df['avatar'] = df['avatar'].fillna('https://robohash.org/default.png?size=50x50')
df['active'] = df['active'].fillna('false')
df['is_admin'] = df['is_admin'].fillna('false')
df['department'] = df['department'].fillna('Other')
df['gender'] = df['gender'].fillna('Other')

df.to_csv('usuarios_completo.csv', index=False)