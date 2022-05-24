import pandas as pd

df = pd.read_csv('usuarios_completo.csv')

df.drop_duplicates(subset=['first_name','last_name','email','company'])
print(df.duplicated().sum())

# df['active'] = df['active'].replace('false', False)
# df['is_admin'] = df['is_admin'].replace('false', False)
# df['gender'] = df['gender'].replace('Other', 'O')

df.to_csv('usuarios_completo.csv', index=False)


