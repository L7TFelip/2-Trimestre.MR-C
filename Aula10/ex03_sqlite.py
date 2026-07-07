import sqlite3
from flask import Flask, jsonify, request

app = Flask(__name__)
DB_NAME = 'loja.db'

@app.route('/produtos', methods=['GET'])
def get_produtos():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM produtos')
    linhas = cursor.fetchall()
    conn.close()
    
    produtos = [{'id': r[0], 'nome': r[1], 'preco': r[2]} for r in linhas]
    return jsonify(produtos), 200

@app.route('/produtos', methods=['POST'])
def post_produto():
    dados = request.get_json()
    
    if not dados or 'preco' not in dados or 'nome' not in dados:
        return jsonify({'erro': 'Nome e preço são obrigatórios.'}), 400
        
    nome = dados['nome']
    preco = dados['preco']
    
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO produtos (nome, preco) VALUES (?, ?)', (nome, preco))
    conn.commit()
    id_inserido = cursor.lastrowid
    conn.close()
    
    return jsonify({'id': id_inserido, 'nome': nome, 'preco': preco}), 201

if __name__ == '__main__':
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
    
    app.run(debug=True)

print("Mr - C")
