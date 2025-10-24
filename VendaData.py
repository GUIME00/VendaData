import pandas as pd # Biblioteca para manipulação de dados
import matplotlib.pyplot as plt # Biblioteca para visualização de dados
import numpy as np # Biblioteca para cálculos numéricos

# 1. Ler o arquivo CSV
dados = pd.read_csv("vendas.csv", parse_dates=['Data_Venda']) # Ler o arquivo CSV e converter a coluna Data_Venda para datetime

# 2. Criar coluna faturamento
dados['Faturamento'] = dados['Quantidade'] * dados['Preço_Unitário']

# 3. Cálculos gerais
faturamento_total = np.sum(dados['Faturamento']) # Faturamento total
media_faturamento = np.mean(dados['Faturamento']) # Faturamento médio por venda
desvio_padrao = np.std(dados['Faturamento'], ddof=1) # Desvio padrão do faturamento
produto_top = dados.groupby('Produto')['Faturamento'].sum().idxmax() # Produto mais lucrativo
ticket_medio = faturamento_total / np.sum(dados['Quantidade']) # Ticket médio
produto_mais_vendido = dados.groupby('Produto')['Quantidade'].sum().idxmax() # Produto mais vendido
variacao_mensal = dados.groupby(dados['Data_Venda'].dt.to_period('M'))['Faturamento'].sum() # Variação mensal do faturamento

print(f"Faturamento total: R$ {faturamento_total:,.2f}")
print(f"Faturamento médio por venda: R$ {media_faturamento:,.2f}")
print(f"Desvio padrão do faturamento: R$ {desvio_padrao:,.2f}")
print(f"Ticket Médio: R$ {ticket_medio:,.2f}")
print(f"Produto mais vendido: {produto_mais_vendido}")
print(f"Produto mais lucrativo: {produto_top}")
print(f"\nVariação mensal: \n===============================\n{variacao_mensal}\n===============================\n") # Variação mensal do faturamento

# Calculo do produto mais vendido em porcentagem
total_vendas = np.sum(dados['Quantidade'])
quantidade_produto = dados.groupby('Produto')['Quantidade'].sum()
porcentagem_vendas = (quantidade_produto / total_vendas) * 100
print("Porcentagem de vendas por produto:")
print(f"===============================\n{porcentagem_vendas}\n===============================\n")

# 4. Coeficiente de Variação do faturamento em porcentagem
coef_variacao = (desvio_padrao / media_faturamento) * 100
print(f"\n===============================\nGrau de variação:\n{coef_variacao:.2f}%\n===============================\n")

# 5. Faturamento por produto 
faturamento_produtos = dados.groupby('Produto')['Faturamento'].sum().sort_values(ascending=False)
print(f"Faturamento dos Produtos:\n===============================\n{faturamento_produtos}\n===============================\n")

# 6. Faturamento mensal
dados['Mês'] = dados['Data_Venda'].dt.to_period('M') # Extrair mês e ano da data de venda
faturamento_mensal = dados.groupby('Mês')['Faturamento'].sum()

# 7. Estatísticas descritivas
print("Estatísticas descritivas do faturamento:")
print(f"===============================\n{dados['Faturamento'].describe()}\n===============================\n")



# 8. Região com maior volume de vendas em porcentagem
vendas_regiao = dados.groupby('Região')['Quantidade'].sum()  # Soma das quantidades vendidas por região
total_vendido = vendas_regiao.sum()  # Total de vendas geral
regiao_top = vendas_regiao.idxmax()  # Região com maior volume de vendas
porcentagem_top = (vendas_regiao.max() / total_vendido) * 100  # Porcentagem da região top

print(f"===============================")
print(f"Região com maior volume de vendas:")
print(f"{regiao_top} — {porcentagem_top:.2f}% do total de vendas")
print(f"===============================\n")

# 9. Plotagem de gráficos baseados nos dados analisados
# Gráfico de barras do faturamento por produto
plt.figure(figsize=(8, 5)) # Tamanho da figura
faturamento_produtos.plot(kind='bar', color='blue') # Tipo de gráfico e cor
plt.title('Faturamento por Produto') # Título do gráfico
plt.xlabel('Produto') # Rótulo do eixo x
plt.ylabel('Faturamento (R$)') # Rótulo do eixo y
plt.xticks(rotation=45) # Rotacionar os rótulos do eixo x
plt.tight_layout() # Ajustar layout
plt.show(block=False) # Exibir gráfico sem bloquear a execução

# Gráfico de linha do faturamento mensal
plt.figure(figsize=(8, 5)) # Tamanho da figura
faturamento_mensal.plot(kind='line', marker='o', color="#00FF00FF") # Tipo de gráfico, marcador e cor
plt.title('Faturamento Mensal') # Título do gráfico
plt.xlabel('Mês') # Rótulo do eixo x
plt.ylabel('Faturamento (R$)') # Rótulo do eixo y
plt.tight_layout() # Ajustar layout
plt.show(block=False) # Exibir gráfico sem bloquear a execução

# Gráfico de pizza mostrando a participação das regiões
plt.figure(figsize=(6, 6))
plt.pie(vendas_regiao, labels=vendas_regiao.index, autopct='%1.1f%%', startangle=90)
plt.title('Participação das Regiões nas Vendas')
plt.tight_layout()
plt.show(block=False)

input("Precione Enter para fechar...")
plt.close('all') # Fechar todos os gráficos abertos

print("Análise concluída!")