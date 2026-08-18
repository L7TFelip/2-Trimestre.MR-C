API Tecnoshopp

API REST desenvolvida em Python com Flask e banco de dados SQLite.

Disciplina: Programação no Desenvolvimento de Sistemas
Professor: Diego da Silva
Integrante: Felipe Neves

Sobre o projeto

Esta API gerencia uma loja de informática. O sistema permite cadastrar categorias e produtos, sendo que cada produto pertence a uma categoria. A API oferece operações de cadastro, consulta, atualização, exclusão, além de rotas com JOIN e filtros para facilitar as buscas.

Tabelas do banco

Tabela "categorias"

Campo| Tipo| Descrição
id| INTEGER| Chave primária (gerada automaticamente)
nome| TEXT| Nome da categoria

Tabela "produtos"

Campo| Tipo| Descrição
id| INTEGER| Chave primária (gerada automaticamente)
nome| TEXT| Nome do produto
preco| REAL| Preço do produto
estoque| INTEGER| Quantidade em estoque
categoria_id| INTEGER| Chave estrangeira que referencia a tabela "categorias"

Relação: Uma categoria pode possuir vários produtos, enquanto cada produto pertence a apenas uma categoria.

Como executar o projeto:

# Instalar o Flask
pip install flask

# Executar a aplicação
python app.py

A API ficará disponível em:

http://127.0.0.1:5000

O banco de dados "loja.db" será criado automaticamente na primeira execução.

Rotas da API:

Categorias

Método| Rota| Descrição
GET| "/categorias"| Lista todas as categorias
GET| "/categorias/<id>"| Busca uma categoria pelo ID
POST| "/categorias"| Cadastra uma categoria
PUT| "/categorias/<id>"| Atualiza uma categoria
DELETE| "/categorias/<id>"| Remove uma categoria

Produtos

Método| Rota| Descrição
GET| "/produtos"| Lista todos os produtos
GET| "/produtos/<id>"| Busca um produto pelo ID
POST| "/produtos"| Cadastra um produto
PUT| "/produtos/<id>"| Atualiza um produto
DELETE| "/produtos/<id>"| Remove um produto

Rotas especiais

Método| Rota| Descrição
GET| "/produtos-completo"| Lista produtos com o nome da categoria (JOIN)
GET| "/categorias/<id>/produtos"| Lista os produtos de uma categoria (filtro por caminho)
GET| "/produtos/busca?nome="| Busca produtos pelo nome utilizando "LIKE" (filtro por query string)


Como testar:

As requisições utilizadas para testar a API estão no arquivo "testes.http".

Exemplo para cadastrar uma categoria:

POST http://127.0.0.1:5000/categorias
Content-Type: application/json

{
    "nome": "Periféricos"
}

Exemplo para cadastrar um produto:

POST http://127.0.0.1:5000/produtos
Content-Type: application/json

{
    "nome": "Mouse Gamer",
    "preco": 149.90,
    "estoque": 20,
    "categoria_id": 1
}

---

Tecnologias utilizadas

- Python 3
- Flask
- SQLite
- JSON
- API REST

---

Integrante
- Felipe Neves

print("Mr - C")
