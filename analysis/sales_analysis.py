import pandas
import sqlite3
import matplotlib.pyplot as plt
import pandas as pd

connector = sqlite3.connect("C:/Users/rafae/PycharmProjects/AnálisedeDados/database/vendas.db")

#criando uma tabela para vizualizar os principais dados
query = """
    SELECT C.NOME AS CLIENTE,
           P.NOME AS PRODUTO,
           V.QUANTIDADE,
           P.PRECO,
           (V.QUANTIDADE * P.PRECO) AS TOTAL,
           V.DATA
    FROM VENDAS V
    JOIN CLIENTES C 
    ON V.ID_CLIENTE = C.ID
    JOIN PRODUTOS P
    ON V.ID_PRODUTO = P.ID
"""

# criando um dataframe em pandas baseado em uma tabela do sql
df_vendas = pandas.read_sql_query(query, connector)

connector.close()
#fazendo as analises com pandas
#1) faturamento total
faturamento_total = df_vendas["TOTAL"].sum()
print(f"faturamento total: R$ {faturamento_total:.2f}")

#faturamento por cliente
faturamento_cliente = df_vendas.groupby("CLIENTE")["TOTAL"].sum().sort_values(ascending=False)
print(faturamento_cliente)

#produto mai vendido
produto_mais_vendido = df_vendas.groupby("PRODUTO")["QUANTIDADE"].sum().sort_values(ascending=False)
print(produto_mais_vendido)

df_vendas["DATA"] = pd.to_datetime(df_vendas["DATA"])

vendas_por_data = df_vendas.groupby("DATA")["TOTAL"].sum()

#Graficos das analises
faturamento_cliente.plot(kind = "bar")
plt.title("Faturamento por Cliente")
plt.xlabel("Cliente")
plt.ylabel("Valor Total (R$)")
plt.tight_layout()
plt.show()

produto_mais_vendido.plot(kind = "bar")
plt.text("Quantidade Vendida por Produto")
plt.xlabel("Produto")
plt.ylabel("Quantidade")
plt.tight_layout()
plt.show()

vendas_por_data.plot(kind = "line")
plt.text("Faturamento ao longo do tempo")
plt.xlabel("Data")
plt.ylabel("Faturamento (R$)")
plt.tight_layout()
plt.show()

