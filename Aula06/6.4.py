class Pagamento:
    def processar(self, valor):
        return valor
class Dinheiro(Pagamento):
    def processar(self, valor):
        return valor * 0.95
class Cartao(Pagamento):
    def processar(self, valor):
        return valor * 1.02 
class Pix(Pagamento):
    def processar(self, valor):
        return valor
formas_pagamento = [
    Dinheiro(),
    Cartao(),
    Pix()
]
valor = 100
for forma in formas_pagamento:
    print(
        f"{forma.__class__.__name__}: R$ {forma.processar(valor):.2f}"
    )
print("Mr - C")
