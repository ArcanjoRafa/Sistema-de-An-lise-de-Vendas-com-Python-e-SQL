import sqlite3

connector = sqlite3.connect("C:/Users/rafae/PycharmProjects/AnálisedeDados/database/vendas.db")
cursor = connector.cursor()

cursor.execute("""
    CREATE TABLE CLIENTES(
	ID INTEGER PRIMARY KEY AUTOINCREMENT,
	NOME TEXT NOT NULL,
	CIDADE TEXT NOT NULL);
""")

cursor.execute("""
    CREATE TABLE PRODUTOS(
	ID INTEGER PRIMARY KEY AUTOINCREMENT,
	NOME TEXT NOT NULL,
	PRECO REAL NOT NULL);
""")

cursor.execute("""
    CREATE TABLE VENDAS(
	ID INTEGER PRIMARY KEY AUTOINCREMENT,
	DATA TEXT,
	QUANTIDADE INTEGER,
	ID_CLIENTE INTEGER,
	ID_PRODUTO INTEGER,
	FOREIGN KEY(ID_CLIENTE)
	REFERENCES CLIENTES(ID),
	FOREIGN KEY(ID_PRODUTO)
	REFERENCES PRODUTOS(ID));
""")

connector.commit()
connector.close()

print("Banco e tabelas criados com sucesso!")