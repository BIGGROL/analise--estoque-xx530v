import pandas as pd
import matplotlib.pyplot as plt

# Lê o arquivo CSV
df = pd.read_csv("dados/xx530v_estoque.csv", sep=";")

print("=" * 50)
print("ANÁLISE DO ESTOQUE XX530V")
print("=" * 50)

# Mostra a tabela
print("\nTabela:")
print(df)

# Total de equipamentos
total = df["saldo"].sum()
print(f"\nTotal de equipamentos: {total}")

# Quantidade de almoxarifados
print(f"Quantidade de almoxarifados: {len(df)}")

# Almoxarifado com maior estoque
maior = df.loc[df["saldo"].idxmax()]

print("\nMaior estoque:")
print(maior["almoxarifado"])
print(f'Saldo: {maior["saldo"]}')

# Média
media = df["saldo"].mean()

print(f"\nMédia de equipamentos por almoxarifado: {media:.2f}")

# Ranking
ranking = df[df["saldo"] > 0].sort_values(by="saldo", ascending=False)
print("\nRanking dos almoxarifados:")

print("\nRanking dos almoxarifados:")

print(ranking[["almoxarifado", "saldo"]])

# Gera o gráfico

plt.figure(figsize=(12,6))

barras = plt.bar(
    df["almoxarifado"],
    df["saldo"],
    color="#2E86DE"
)

plt.title("Estoque de Roteadores TP-Link XX530V por Almoxarifado", fontsize=16)

plt.xlabel("Almoxarifado")

plt.ylabel("Quantidade")

plt.xticks(rotation=35, ha="right")

# Escreve o valor em cima das barras
for barra in barras:
    altura = barra.get_height()
    plt.text(
        barra.get_x() + barra.get_width()/2,
        altura + 0.3,
        int(altura),
        ha="center"
    )

plt.grid(axis="y", linestyle="--", alpha=0.3)

plt.tight_layout()

plt.savefig("graficos/estoque_xx530v.png", dpi=300)

plt.show()
print(ranking[["almoxarifado", "saldo"]])# Gera o gráfico
