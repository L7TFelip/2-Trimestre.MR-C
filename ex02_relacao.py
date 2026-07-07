from flask import jsonify
from ex01_relacao import app, db, Livro, Autor

@app.route('/livros-completo', methods=['GET'])
def listar_livros_completo():
    # Realiza o JOIN entre as tabelas Livro e Autor
    resultados = db.session.query(Livro.titulo, Autor.nome)\
        .join(Autor, Livro.autor_id == Autor.id).all()
    
    # Formata o resultado em uma lista de dicionários (JSON)
    lista_livros = [{"titulo": titulo, "autor": nome} for titulo, nome in resultados]
    
    return jsonify(lista_livros)

if __name__ == '__main__':
    app.run(debug=True)

print("Mr - c")