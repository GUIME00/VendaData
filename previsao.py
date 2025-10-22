import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt

# --- 1) Ler o CSV ---
df = pd.read_csv("vendas.csv", parse_dates=["Data_Venda"])

# --- 2) Criar coluna de total da venda ---
df["Total_Venda"] = df["Quantidade"] * df["Preço_Unitário"]

# --- 3) Criar colunas de data ---
df["Ano"] = df["Data_Venda"].dt.year
df["Mes"] = df["Data_Venda"].dt.month

# --- 4) Selecionar variáveis ---
X = df[["Quantidade", "Preço_Unitário", "Ano", "Mes"]]
y = df["Total_Venda"]

# --- 5) Dividir em treino e teste ---
X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.2, random_state=42)

# --- 6) Criar e treinar o modelo ---
modelo = RandomForestRegressor(random_state=42)
modelo.fit(X_treino, y_treino)

# --- 7) Fazer previsões ---
y_pred = modelo.predict(X_teste)

# --- 8) Avaliar ---
mae = mean_absolute_error(y_teste, y_pred)
mse = mean_squared_error(y_teste, y_pred)
r2 = r2_score(y_teste, y_pred)

print("=== RESULTADOS DO MODELO ===")
print(f"Erro Absoluto Médio (MAE): {mae:.2f}")
print(f"Erro Quadrático Médio (MSE): {mse:.2f}")
print(f"Coeficiente R²: {r2:.3f}")

# --- 9) Gráfico de comparação ---
plt.figure(figsize=(8,5))
plt.scatter(y_teste, y_pred, color="purple", alpha=0.6)
plt.plot([y_teste.min(), y_teste.max()], [y_teste.min(), y_teste.max()], 'r--')
plt.title("Comparação: Valores Reais x Previstos")
plt.xlabel("Valor Real da Venda")
plt.ylabel("Valor Previsto da Venda")
plt.grid(True)
plt.tight_layout()
plt.show()

# --- 10) Exemplo de previsão nova ---
novo_exemplo = pd.DataFrame({
    "Quantidade": [3],
    "Preço_Unitário": [200.0],
    "Ano": [2025],
    "Mes": [10]
})

previsao = modelo.predict(novo_exemplo)
print("\nExemplo de previsão:")
print(f"Valor total estimado da venda: R$ {previsao[0]:.2f}")