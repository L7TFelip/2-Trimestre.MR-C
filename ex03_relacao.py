from flask import jsonify, request
from ex01_relacao import app, db, Livro

# Rota 1: Filtrar livros de um autor específico pelo ID
@app.route('/autores/<int:autor_id>/livros', methods=['GET'])
def livros_por_autor(autor_id):
    livros = Livro.query.filter_by(autor_id=autor_id).all()
    
    lista = [{"id": l.id, "titulo": l.titulo} for l in livros]
    return jsonify(lista)

# Rota 2: Buscar livros por título usando LIKE (Query String)
# Exemplo de uso: /livros/busca?titulo=Casmurro
@app.route('/livros/busca', methods=['GET'])
def buscar_livros():
    # Obtém o parâmetro 'titulo' da URL. Se não existir, assume string vazia
    termo_busca = request.args.get('titulo', '')
    
    # Filtro com LIKE (o % indica que pode ter qualquer texto antes ou depois)
    livros = Livro.query.filter(Livro.titulo.like(f"%{termo_busca}%")).all()
    
    lista = [{"id": l.id, "titulo": l.titulo, "autor_id": l.autor_id} for l in livros]
    return jsonify(lista)

if __name__ == '__main__':
    app.run(debug=True)

print("Mr - C")