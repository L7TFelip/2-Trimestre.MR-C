from flask import Flask, jsonify

app = Flask(__name__)


produtos = [
    {"id": 1, "nome": "Teclado Mecânico", "preco": 259.50, "disponivel": True},
    {"id": 2, "nome": "Mouse Gamer", "preco": 153.00, "disponivel": False},
    {"id": 3, "nome": "Monitor 144Hz", "preco": 1280.09, "disponivel": True},
    {"id": 4, "nome": "Headset", "preco": 350.70, "disponivel": True}
]

@app.route('/produtos/<int:id>', methods=['GET'])
def obter_produto_por_id(id):
    for produto in produtos:
        if produto["id"] == id:
            return jsonify(produto)
    
    return jsonify({"erro": "Produto nao encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True)