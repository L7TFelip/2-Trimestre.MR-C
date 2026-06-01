class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        
    def calcular_desconto(self, percentual):
        valor_desconto = self.preco * (percentual / 100)
        preco_final = self.preco - valor_desconto
        return preco_final

p1 = Produto("Notebook", 600.0)
preco_final = p1.calcular_desconto(67.0)
print(f"O preço final do {p1.nome} é R$ {preco_final:.2f}")
