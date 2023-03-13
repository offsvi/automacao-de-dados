import pandas as pd

# Ler o arquivo CSV
df = pd.read_csv('dados.csv')

# Exibir as primeiras 5 linhas dos dados
print(df.head())

# Calcular o preço médio
preco_medio = df['preco'].mean()
print('Preço médio:', preco_medio)

# Salvar os resultados em um novo arquivo CSV 
df.to_csv('resultado.csv', index=False)
