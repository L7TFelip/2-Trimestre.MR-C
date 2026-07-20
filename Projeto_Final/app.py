from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

BANCO = "loja.db"


def conectar():
    conn = sqlite3.connect(BANCO)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def criar_banco():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS categorias(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco REAL NOT NULL,
            estoque INTEGER NOT NULL,
            categoria_id INTEGER NOT NULL,
            FOREIGN KEY(categoria_id)
            REFERENCES categorias(id)
            ON DELETE CASCADE
        )
    """)

    conn.commit()
    conn.close()


criar_banco()

@app.route("/categorias", methods=["GET"])
def listar_categorias():
    conn = conectar()
    categorias = conn.execute("SELECT * FROM categorias").fetchall()
    conn.close()

    return jsonify([dict(c) for c in categorias])


@app.route("/categorias/<int:id>", methods=["GET"])
def buscar_categoria(id):
    conn = conectar()
    categoria = conn.execute(
        "SELECT * FROM categorias WHERE id=?",
        (id,)
    ).fetchone()
    conn.close()

    if categoria is None:
        return jsonify({"erro": "Categoria não encontrada"}), 404

    return jsonify(dict(categoria))


@app.route("/categorias", methods=["POST"])
def criar_categoria():

    dados = request.get_json()

    if not dados or "nome" not in dados:
        return jsonify({"erro": "Nome obrigatório"}), 400

    conn = conectar()

    cursor = conn.execute(
        "INSERT INTO categorias(nome) VALUES(?)",
        (dados["nome"],)
    )

    conn.commit()

    novo_id = cursor.lastrowid

    conn.close()

    return jsonify({"id": novo_id, "mensagem": "Categoria criada"}), 201


@app.route("/categorias/<int:id>", methods=["PUT"])
def atualizar_categoria(id):

    dados = request.get_json()

    conn = conectar()

    existe = conn.execute(
        "SELECT * FROM categorias WHERE id=?",
        (id,)
    ).fetchone()

    if existe is None:
        conn.close()
        return jsonify({"erro": "Categoria não encontrada"}), 404

    conn.execute(
        "UPDATE categorias SET nome=? WHERE id=?",
        (dados["nome"], id)
    )

    conn.commit()
    conn.close()

    return jsonify({"mensagem": "Categoria atualizada"})


@app.route("/categorias/<int:id>", methods=["DELETE"])
def excluir_categoria(id):

    conn = conectar()

    cursor = conn.execute(
        "DELETE FROM categorias WHERE id=?",
        (id,)
    )

    conn.commit()

    if cursor.rowcount == 0:
        conn.close()
        return jsonify({"erro": "Categoria não encontrada"}), 404

    conn.close()

    return jsonify({"mensagem": "Categoria excluída"})

@app.route("/produtos", methods=["GET"])
def listar_produtos():

    conn = conectar()

    produtos = conn.execute(
        "SELECT * FROM produtos"
    ).fetchall()

    conn.close()

    return jsonify([dict(p) for p in produtos])


@app.route("/produtos/<int:id>", methods=["GET"])
def buscar_produto(id):

    conn = conectar()

    produto = conn.execute(
        "SELECT * FROM produtos WHERE id=?",
        (id,)
    ).fetchone()

    conn.close()

    if produto is None:
        return jsonify({"erro": "Produto não encontrado"}), 404

    return jsonify(dict(produto))


@app.route("/produtos", methods=["POST"])
def criar_produto():

    dados = request.get_json()

    campos = ["nome", "preco", "estoque", "categoria_id"]

    if not dados or not all(c in dados for c in campos):
        return jsonify({"erro": "Dados inválidos"}), 400

    conn = conectar()

    categoria = conn.execute(
        "SELECT * FROM categorias WHERE id=?",
        (dados["categoria_id"],)
    ).fetchone()

    if categoria is None:
        conn.close()
        return jsonify({"erro": "Categoria inexistente"}), 404

    cursor = conn.execute("""
        INSERT INTO produtos
        (nome,preco,estoque,categoria_id)
        VALUES(?,?,?,?)
    """, (
        dados["nome"],
        dados["preco"],
        dados["estoque"],
        dados["categoria_id"]
    ))

    conn.commit()

    novo_id = cursor.lastrowid

    conn.close()

    return jsonify({"id": novo_id, "mensagem": "Produto criado"}), 201


@app.route("/produtos/<int:id>", methods=["PUT"])
def atualizar_produto(id):

    dados = request.get_json()

    conn = conectar()

    existe = conn.execute(
        "SELECT * FROM produtos WHERE id=?",
        (id,)
    ).fetchone()

    if existe is None:
        conn.close()
        return jsonify({"erro": "Produto não encontrado"}), 404

    conn.execute("""
        UPDATE produtos
        SET nome=?,preco=?,estoque=?,categoria_id=?
        WHERE id=?
    """, (
        dados["nome"],
        dados["preco"],
        dados["estoque"],
        dados["categoria_id"],
        id
    ))

    conn.commit()
    conn.close()

    return jsonify({"mensagem": "Produto atualizado"})


@app.route("/produtos/<int:id>", methods=["DELETE"])
def excluir_produto(id):

    conn = conectar()

    cursor = conn.execute(
        "DELETE FROM produtos WHERE id=?",
        (id,)
    )

    conn.commit()

    if cursor.rowcount == 0:
        conn.close()
        return jsonify({"erro": "Produto não encontrado"}), 404

    conn.close()

    return jsonify({"mensagem": "Produto excluído"})


@app.route("/produtos-completo", methods=["GET"])
def produtos_completo():

    conn = conectar()

    produtos = conn.execute("""
        SELECT
            produtos.id,
            produtos.nome,
            produtos.preco,
            produtos.estoque,
            categorias.nome AS categoria
        FROM produtos
        INNER JOIN categorias
        ON produtos.categoria_id = categorias.id
    """).fetchall()

    conn.close()

    return jsonify([dict(p) for p in produtos])

@app.route("/categorias/<int:id>/produtos", methods=["GET"])
def produtos_categoria(id):

    conn = conectar()

    produtos = conn.execute("""
        SELECT *
        FROM produtos
        WHERE categoria_id=?
    """, (id,)).fetchall()

    conn.close()

    return jsonify([dict(p) for p in produtos])

@app.route("/produtos/busca", methods=["GET"])
def busca_produtos():

    nome = request.args.get("nome", "")

    conn = conectar()

    produtos = conn.execute("""
        SELECT *
        FROM produtos
        WHERE nome LIKE ?
    """, (f"%{nome}%",)).fetchall()

    conn.close()

    return jsonify([dict(p) for p in produtos])


if __name__ == "__main__":
    app.run(debug=True)
