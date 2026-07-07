import sqlite3

conn = sqlite3.connect('loja.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        preco REAL NOT NULL
    )
''')

produtos = [
    ('Notebook', 3500.00),
    ('Smartphone', 1500.00),
    ('Fone de Ouvido', 150.00)
]

cursor.executemany('INSERT INTO produtos (nome, preco) VALUES (?, ?)', produtos)
conn.commit()
conn.close()

print("Mr - C")