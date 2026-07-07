from flask import Flask, jsonify, request

app = Flask(__name__)

produtos = [
    {"id": 1, "nome": "Teclado Mecânico", "preco": 250.0},
    {"id": 2, "nome": "Mouse Gamer", "preco": 150.0}
]

@app.route('/produtos/<int:id>', methods=['PUT'])
def atualizar_produto(id):
    dados = request.get_json()
    produto = next((p for p in produtos if p['id'] == id), None)
    if not produto:
        return jsonify({"erro": "Produto não encontrado"}), 404
    produto['nome'] = dados.get('nome', produto['nome'])
    produto['preco'] = dados.get('preco', produto['preco'])
    return jsonify(produto), 200

@app.route('/produtos/<int:id>', methods=['DELETE'])
def apagar_produto(id):
    global produtos
    produto = next((p for p in produtos if p['id'] == id), None)
    
    if not produto:
        return jsonify({"erro": "Produto não encontrado"}), 404

    produtos = [p for p in produtos if p['id'] != id]
    return jsonify({"mensagem": "Produto apagado com sucesso"}), 200

if __name__ == '__main__':
    app.run(debug=True)

    print("Mr - C")