import sqlite3

connector = sqlite3.connect("C:/Users/rafae/PycharmProjects/AnálisedeDados/database/vendas.db")
cursor = connector.cursor()

#tabela de todas as vendas
cursor.execute("""
    SELECT C.NOME AS CLIENTE,
    P.NOME AS PRODUTO,
    V.QUANTIDADE,
    P.PRECO,
    (V.QUANTIDADE * P.PRECO) AS TOTAL,
     V.DATA
    FROM VENDAS V
    JOIN CLIENTES C
    ON C.ID = V.ID_CLIENTE
    JOIN PRODUTOS P
    ON V.ID_PRODUTO = P.ID;
""")

vendas = cursor.fetchall()

for venda in vendas:
    print(venda)

#tabela do faturamento total de vendas
cursor.execute("""
    SELECT SUM(P.PRECO * V.QUANTIDADE) AS FATURAMENTO_TOTAL
    FROM VENDAS V
    JOIN PRODUTOS P
    ON V.ID_PRODUTO = P.ID;
""")

faturamento = cursor.fetchone()[0]
print(f"faturamento total: R$ {faturamento}")

#tabela do faturamento por cliente
cursor.execute("""
    SELECT C.NOME,SUM(V.QUANTIDADE * P.PRECO) AS TOTAL
    FROM VENDAS V
    JOIN CLIENTES C
    ON V.ID_CLIENTE = C.ID
    JOIN PRODUTOS P
    ON V.ID_PRODUTO = P.ID
    GROUP BY C.NOME
    ORDER BY TOTAL DESC;
""")

clientes =[cliente for cliente in cursor.fetchall()]

for cliente in clientes:
    print(cliente)

#tabela dos produtos mais vendidos
cursor.execute("""
    SELECT P.NOME, SUM(QUANTIDADE * PRECO) AS TOTAL
    FROM VENDAS V
    JOIN PRODUTO P
    ON V.ID_PRODUTO = P.ID
    GROUP BY P.NOME
    ORDER BY TOTAL DESC
    LIMIT 1;
""")

produto = cursor.fetchone()
print(f"Produto mais vendido: {produto}")
