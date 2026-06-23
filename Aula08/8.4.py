from flask import Flask, jsonify

app = Flask(__name__)

produtos = [
    {"id": 1, "nome": "Teclado Mecânico", "preco": 250.50, "disponivel": True},
    {"id": 2, "nome": "Mouse Gamer", "preco": 150.80, "disponivel": False},
    {"id": 3, "nome": "Monitor 144Hz", "preco": 1260.00, "disponivel": True},
    {"id": 4, "nome": "Headset Bluetooth", "preco": 358.00, "disponivel": True}
]

@app.route('/produtos/disponiveis', methods=['GET'])
def listar_disponiveis():

    disponiveis = [p for p in produtos if p["disponivel"] == True]
    return jsonify(disponiveis)

if __name__ == '__main__':
    app.run(debug=True)
