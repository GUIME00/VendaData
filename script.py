import pandas as pd
import matplotlib.pyplot as plt

# 1. Ler o arquivo CSV
dados = pd.read_csv("vendas.csv", parse_dates=['Data_Venda'])

# 2. Criar coluna faturamento
dados['Faturamento'] = dados['Quantidade'] * dados['Preço_Unitário']

# 3. Cálculos gerais
faturamento_total = dados['Faturamento'].sum()
media_faturamento = dados['Faturamento'].mean()
produto_top = dados.groupby('Produto')['Faturamento'].sum().idxmax()
ticket_medio = faturamento_total / dados['Quantidade'].sum()
variacao_mensal = dados.groupby(dados['Data_Venda'].dt.to_period('M'))['Faturamento'].sum()

print(f"Faturamento total: R$ {faturamento_total:,.2f}")
print(f"Faturamento médio por venda: R$ {media_faturamento:,.2f}")
print(f"Produto mais lucrativo: {produto_top}")
print(f"Ticket Médio: R$ {ticket_medio}")
print(f"Produto mais vendido: {produto_top}")
print(f"\nVariação mensal: \n===============================\n{variacao_mensal}\n===============================\n")

# 4. Faturamento por produto
faturamento_produtos = dados.groupby('Produto')['Faturamento'].sum().sort_values(ascending=False)
print(f"Faturamento dos Produtos:\n===============================\n{faturamento_produtos}\n===============================\n")

# 5. Faturamento mensal
dados['Mês'] = dados['Data_Venda'].dt.to_period('M')
faturamento_mensal = dados.groupby('Mês')['Faturamento'].sum()

# 6. Exibir estatísticas descritivas
print("Estatísticas descritivas do faturamento:")
print(f"===============================\n{dados['Faturamento'].describe()}\n===============================\n")

# 7. Plotagem
plt.figure(figsize=(8, 5))
faturamento_produtos.plot(kind='bar', color='blue')
plt.title('Faturamento por Produto')
plt.xlabel('Produto')
plt.ylabel('Faturamento (R$)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show(block=False)

plt.figure(figsize=(8, 5))
faturamento_mensal.plot(kind='line', marker='o', color='skyblue')
plt.title('Faturamento Mensal')
plt.xlabel('Mês')
plt.ylabel('Faturamento (R$)')
plt.tight_layout()
plt.show(block=False)

input("Precione Enter para fechar...")
plt.close('all')

print("Análise concluída!")