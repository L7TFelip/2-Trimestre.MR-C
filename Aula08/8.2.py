from flask import Flask, jsonify

app = Flask(__name__)

produtos = [
    {"id": 1, "nome": "Teclado Mecânico", "preco": 2540.00, "disponivel": True},
    {"id": 2, "nome": "Mouse Gamer", "preco": 1580.00, "disponivel": False},
    {"id": 3, "nome": "Monitor 144Hz", "preco": 1270.00, "disponivel": True},
    {"id": 4, "nome": "Headset", "preco": 359.00, "disponivel": True}
]

@app.route('/produtos', methods=['GET'])
def listar_produtos():
    return jsonify(produtos)

if __name__ == '__main__':
    app.run(debug=True)
