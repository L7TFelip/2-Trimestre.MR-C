import sqlite3

conn = sqlite3.connect('loja.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM produtos')
produtos = cursor.fetchall()

for prod in produtos:
    print(f"ID: {prod[0]} | Nome: {prod[1]} | Preço: R$ {prod[2]:.2f}")

conn.close()

print("Mr - C")
