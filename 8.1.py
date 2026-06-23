from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/produto', methods=['GET'])
def obter_produto():
    produto = {
        "id": 1,
        "nome": "Teclado Mecânico",
        "preco": 250.00,
        "disponivel": True
    }
    return jsonify(produto)

if __name__ == '__main__':
    app.run(debug=True)