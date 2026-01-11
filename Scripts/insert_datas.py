import sqlite3

connector = sqlite3.connect("C:/Users/rafae/PycharmProjects/AnálisedeDados/database/vendas.db")
cursor = connector.cursor()

#---insert dados na tabela CLIENTE---

clientes = [
    ("Carlos","Rio de Janeiro"),
    ("Patricia","Campo Grande"),
    ("Matheus","Belo Horizonte"),
    ("Jaqueline","São Paulo"),
    ("Lucas","Cuiabá")
]

cursor.executemany("""
    INSERT INTO CLIENTES(NOME, CIDADE) VALUES(?, ?)
""", clientes)

#---insert dados na tabela PRODUTOS---

produtos = [
    ("Notebook",3500.00),
    ("Mouse",120.00),
    ("Teclado",250.00),
    ("Monitor",1100.00),
    ("Headset",300.00)
]

cursor.executemany("""
    INSERT INTO PRODUTOS(NOME, PRECO) VALUES(?, ?)
""",produtos)

#---insert dados na tabela VENDAS---

vendas = [
    (1, 1, "2025-12-10", 1),
    (2, 2, "2025-11-06", 2),
    (3, 3, "2026-01-02", 2),
    (1, 4, "2026-01-05", 1),
    (4, 5, "2025-09-24", 3)
]

cursor.executemany("""
    INSERT INTO VENDAS(ID_CLIENTE, ID_PRODUTO, DATA, QUANTIDADE) VALUES(?, ?, ?, ?)
""",vendas)

connector.commit()
connector.close()

print("Dados inseridos com sucesso!")