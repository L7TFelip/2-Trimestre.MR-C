class Instrumento:
    def tocar(self):
        print("Som de instrumento")


class Violao(Instrumento):
    def tocar(self):
        print("Tocando violão: plim plim")


class Bateria(Instrumento):
    def tocar(self):
        print("Tocando bateria: tum tum")


class Piano(Instrumento):
    def tocar(self):
        print("Tocando piano: dó ré mi")


instrumentos = [
    Violao(),
    Bateria(),
    Piano()
]

for instrumento in instrumentos:
    instrumento.tocar()

print("Mr - C")
