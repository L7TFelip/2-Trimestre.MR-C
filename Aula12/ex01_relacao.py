from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///biblioteca.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Autor(db.Model):
    __tablename__ = 'autores'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    livros = db.relationship('Livro', backref='autor', lazy=True)

class Livro(db.Model):
    __tablename__ = 'livros'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(150), nullable=False)
    autor_id = db.Column(db.Integer, db.ForeignKey('autores.id'), nullable=False)

with app.app_context():
    db.create_all()
    
    if not Autor.query.first():

        autor1 = Autor(nome="Machado de Assis")
        autor2 = Autor(nome="Clarice Lispector")
        db.session.add_all([autor1, autor2])
        db.session.commit()
        
        # 2. Inserindo 3 livros ligados a eles
        livro1 = Livro(titulo="Dom Casmurro", autor_id=autor1.id)
        livro2 = Livro(titulo="Memórias Póstumas de Brás Cubas", autor_id=autor1.id)
        livro3 = Livro(titulo="A Hora da Estrela", autor_id=autor2.id)
        db.session.add_all([livro1, livro2, livro3])
        
        db.session.commit()
        print("Banco de dados criado e populado com sucesso!")

if __name__ == '__main__':
    app.run(debug=True)

print("Mr - C")
