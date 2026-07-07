import sqlite3
from flask import Flask, jsonify, request

app = Flask(__name__)
DATABASE = 'tarefas.db'

def init_db():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tarefas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                feita INTEGER NOT NULL DEFAULT 0
            )
        ''')
        conn.commit()

init_db()

def db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# 1. READ ALL (GET /tarefas)
@app.route('/tarefas', methods=['GET'])
def listar_tarefas():
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tarefas')
    tarefas = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return jsonify(tarefas), 200

@app.route('/tarefas', methods=['POST'])
def criar_tarefa():
    dados = request.get_json()
    titulo = dados.get('titulo')
    feita = dados.get('feita', 0)
    
    if not titulo:
        return jsonify({"erro": "O campo 'titulo' é obrigatório"}), 400
        
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tarefas (titulo, feita) VALUES (?, ?)', (titulo, feita))
    conn.commit()
    novo_id = cursor.lastrowid
    conn.close()
    
    return jsonify({"id": novo_id, "titulo": titulo, "feita": feita}), 201

@app.route('/tarefas/<int:id>', methods=['PUT'])
def atualizar_tarefa(id):
    dados = request.get_json()
    
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tarefas WHERE id = ?', (id,))
    tarefa = cursor.fetchone()
    
    if not tarefa:
        conn.close()
        return jsonify({"erro": "Tarefa não encontrada"}), 404
        
    titulo = dados.get('titulo', tarefa['titulo'])
    feita = dados.get('feita', tarefa['feita'])
    
    cursor.execute('UPDATE tarefas SET titulo = ?, feita = ? WHERE id = ?', (titulo, feita, id))
    conn.commit()
    conn.close()
    
    return jsonify({"id": id, "titulo": titulo, "feita": feita}), 200

@app.route('/tarefas/<int:id>', methods=['DELETE'])
def apagar_tarefa(id):
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tarefas WHERE id = ?', (id,))
    tarefa = cursor.fetchone()
    
    if not tarefa:
        conn.close()
        return jsonify({"erro": "Tarefa não encontrada"}), 404
        
    cursor.execute('DELETE FROM tarefas WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    
    return jsonify({"mensagem": "Tarefa apagada com sucesso"}), 200

if __name__ == '__main__':
    app.run(debug=True)

print("Mr - C")