import pandas as pd

df = pd.read_csv("vendas.csv", parse_dates=['Data_Venda'])
print(df)
print(f"Primeiras 5 linhas de DataFrame de vendas:\n{df.head()}")

print(f"\nÚltimas 5 linhas de DataFrame de vendas:\n{df.tail()}")

print(f"\nInformações sobre o DataFrame: {df.info()}")

print(f"\nO DataFrame de vendas têm:\n{df.shape[0]} linhas e {df.shape[1]} colunas.")

print("\nEstatística descritiva do DataFrame:")
print(df.describe())


print("\nInformações do índice:")
print(df.index)