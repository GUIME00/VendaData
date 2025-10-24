# 📊 Análise de Vendas com Python

Este projeto realiza uma análise completa de dados de vendas a partir de um arquivo **CSV**, gerando **estatísticas, métricas financeiras e gráficos** para visualização dos resultados.

## 🚀 Funcionalidades

- Leitura e tratamento dos dados com **pandas**
- Cálculo de:
  - ✅ Faturamento total  
  - ✅ Faturamento médio  
  - ✅ Desvio padrão e coeficiente de variação  
  - ✅ Produto mais lucrativo  
  - ✅ Produto mais vendido  
  - ✅ Ticket médio  
- Análise de **variação mensal de faturamento**
- Geração de **gráficos**:
  - Faturamento por produto (barras)
  - Faturamento mensal (linha)
  - Participação das Regiões nas Vendas (pizza)

---

## 🧩 Tecnologias utilizadas

- [Python 3](https://www.python.org/)
- [Pandas](https://pandas.pydata.org/)
- [NumPy](https://numpy.org/)
- [Matplotlib](https://matplotlib.org/)

---

## 📁 Estrutura do projeto

📂 analise_vendas/
├── vendas.csv # Arquivo com os dados de vendas
├── VendaData.py # Script principal de análise
└── README.md # Documentação do projeto


---

## 📊 Exemplo de saída (terminal)

Faturamento total: R$ 25.430,00
Faturamento médio por venda: R$ 423,83
Desvio padrão do faturamento: R$ 150,23
Produto mais lucrativo: Teclado Mecânico
Ticket Médio: R$ 180,50
Produto mais vendido: Mouse Gamer


---

## 📈 Gráficos gerados

- **Faturamento por produto** (gráfico de barras)
- **Faturamento mensal** (gráfico de linha)
- **Participação das Regiões nas Vendas** (pizza)

Os gráficos são exibidos automaticamente ao executar o script.

---

## ⚙️ Como executar o projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/GUIME00/VendaData.git

   cd VendaData

   pip install pandas matplotlib numpy

ID_Venda,Data_Venda,Produto,Categoria,Quantidade,Preço_Unitário,Vendedor,Região

python analise_vendas.py

Criado com 💙 por Guilherme Brasil Pereira

📧 E-mail: guibrasilpereira@gmail.com

