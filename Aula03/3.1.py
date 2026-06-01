class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
Produto1 = Produto("Coxinha",5.0)
Produto2 = Produto("Computador",2500.0)
print(Produto1.nome, Produto1.preco)
print(Produto2.nome, Produto2.preco)
