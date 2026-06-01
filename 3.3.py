class Carro:
    def __init__(self, marca, modelo, velocidade):
        self.marca = marca
        self.modelo = modelo
        self.velocidade = velocidade
    def acelerar(self):
        self.velocidade+=10
    def frear(self):
        self.velocidade-=10
        if self.velocidade < 0:
            self.velocidade = 0

car1 = Carro("Renault","Logan",0)

for i in range(3):
    car1.acelerar()
car1.frear()

print(car1.velocidade)