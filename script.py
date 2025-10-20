import pandas as pd
import matplotlib.pyplot as plt

# 1. Ler o arquivo CSV
# Certifique-se de que o arquivo vendas.csv está na mesma pasta do script
dados = pd.read_csv("vendas.csv", parse_dates=['Data_Venda'])

# 2. Criar coluna de faturamento total
dados['Faturamento'] = dados['Quantidade'] * dados['Preço_Unitário']

# 3. Exibir as 5 primeiras linhas
print("Prévia dos dados:")
print(dados.head())
print("\n")

# 4. Cálculos gerais
faturamento_total = dados['Faturamento'].sum()
media_faturamento = dados['Faturamento'].mean()
produto_top = dados.groupby('Produto')['Faturamento'].sum().idxmax()

print(f"💰 Faturamento total: R$ {faturamento_total:,.2f}")
print(f"📊 Faturamento médio por venda: R$ {media_faturamento:,.2f}")
print(f"🏆 Produto mais lucrativo: {produto_top}")
print("\n")

# 5. Faturamento por produto
faturamento_produto = dados.groupby('Produto')['Faturamento'].sum().sort_values(ascending=False)

# 6. Faturamento mensal
dados['Data_Venda'] = pd.to_datetime(dados['Data_Venda'])
dados['Mês'] = dados['Data_Venda'].dt.to_period('M')
faturamento_mensal = dados.groupby('Mês')['Faturamento'].sum()

# 7. Exibir estatísticas descritivas
print("📈 Estatísticas descritivas do faturamento:")
print(dados['Faturamento'].describe())
print("\n")

# 8. Plotagem
plt.figure(figsize=(8, 5))
faturamento_produto.plot(kind='bar', color='skyblue')
plt.title('Faturamento por Produto')
plt.xlabel('Produto')
plt.ylabel('Faturamento (R$)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show(block=False)

plt.figure(figsize=(8, 5))
faturamento_mensal.plot(kind='line', marker='o', color='orange')
plt.title('Faturamento Mensal')
plt.xlabel('Mês')
plt.ylabel('Faturamento (R$)')
plt.tight_layout()
plt.show(block=False)

input("Precione Enter para fechar...")
plt.close('all')

print("Análise concluída!")