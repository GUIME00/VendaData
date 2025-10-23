import pandas as pd
import matplotlib.pyplot as plt

def carregar_dados(caminho_csv):
    try:
        df = pd.read_csv(caminho_csv)
        print("✅ Dados carregados com sucesso!\n")
        return df
    except FileNotFoundError:
        print("❌ Arquivo não encontrado. Verifique o caminho informado.")
        return None

def preparar_dados(df):
    df['Data_Venda'] = pd.to_datetime(df['Data_Venda'])
    df['Faturamento'] = df['Quantidade'] * df['Preço_Unitário']
    return df

def calcular_metricas(df):
    total_vendas = df['Faturamento'].sum()
    media_faturamento = df['Faturamento'].mean()
    ticket_medio = total_vendas / df['Quantidade'].sum()
    produto_top = df.groupby('Produto')['Faturamento'].sum().idxmax()

    variacao_mensal = df.groupby(df['Data_Venda'].dt.to_period('M'))['Faturamento'].sum()

    print("===== MÉTRICAS DE VENDAS =====")
    print(f"Total de Faturamento: R$ {total_vendas:,.2f}")
    print(f"Média de Faturamento: R$ {media_faturamento:,.2f}")
    print(f"Ticket Médio: R$ {ticket_medio:,.2f}")
    print(f"Produto mais vendido: {produto_top}")
    print("\n===== Variação Mensal =====")
    print(variacao_mensal)
    print("=============================\n")

def gerar_graficos(df):

    produtos = df.groupby('Produto')['Faturamento'].sum().sort_values(ascending=False)
    produtos.plot(kind='bar', figsize=(8, 4), title='Faturamento por Produto')
    plt.ylabel("Faturamento (R$)")
    plt.xlabel("Produto")
    plt.tight_layout()
    plt.show()

    faturamento_mensal = df.groupby(df['Data_Venda'].dt.to_period('M'))['Faturamento'].sum()
    faturamento_mensal.plot(kind='line', marker='o', figsize=(8, 4), title='Faturamento Mensal')
    plt.ylabel("Faturamento (R$)")
    plt.xlabel("Mês")
    plt.tight_layout()
    plt.show()

    top_vendedores = df.groupby('Vendedor')['Faturamento'].sum().sort_values(ascending=False)
    plt.figure(figsize=(8, 5))
    top_vendedores.plot(kind='pie',autopct='%1.1f%%',startangle=90,ylabel='')
    plt.title('Participação dos Vendedores no Faturamento')
    plt.tight_layout()
    plt.show(block=False)


def main():
    print("=== VendaData - Sistema de Análise Comercial ===")
    caminho = input("Digite o caminho do arquivo CSV de vendas: ")

    df = carregar_dados(caminho)
    if df is not None:
        df = preparar_dados(df)
        calcular_metricas(df)
        gerar_graficos(df)


if __name__ == "__main__":
    main()