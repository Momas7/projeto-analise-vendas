import pandas as pd
import random
from datetime import datetime, timedelta

# Quantidade de registros
NUM_REGISTROS = 1000

# Listas de dados
produtos = [
    ("Notebook", "Eletrônicos", 3500),
    ("Mouse", "Eletrônicos", 80),
    ("Teclado", "Eletrônicos", 120),
    ("Monitor", "Eletrônicos", 1800),
    ("Cadeira", "Escritório", 900),
    ("Mesa", "Escritório", 1200)
]

vendedores = ["Lucas", "Ana", "Pedro", "Mariana"]
regioes = ["Sudeste", "Sul", "Nordeste"]

data_inicio = datetime(2023, 1, 1)
data_fim = datetime(2024, 12, 31)

dados = []

for i in range(1, NUM_REGISTROS + 1):
    produto, categoria, preco = random.choice(produtos)
    quantidade = random.randint(1, 5)
    faturamento = quantidade * preco

    data_venda = data_inicio + timedelta(
        days=random.randint(0, (data_fim - data_inicio).days)
    )

    dados.append([
        i,
        data_venda,
        produto,
        categoria,
        quantidade,
        preco,
        random.choice(vendedores),
        random.choice(regioes),
        faturamento
    ])

colunas = [
    "id_venda",
    "data_venda",
    "produto",
    "categoria",
    "quantidade",
    "preco_unitario",
    "vendedor",
    "regiao",
    "faturamento"
]

df = pd.DataFrame(dados, columns=colunas)

# Salvar CSV
df.to_csv("../dados/vendas_geradas.csv", index=False, encoding="utf-8")

print("Arquivo vendas_geradas.csv criado com sucesso!")
