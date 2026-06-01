class Veiculo:
    def __init__(self, marca, year):
        self.marca = marca
        self.ano = year

    def informacoes(self):
        print(f"Marca: {self.marca} | Ano: {self.ano}")


class Carro(Veiculo):
    def __init__(self, marca, ano, portas):

        super().__init__(marca, ano)
        self.portas = portas


class Moto(Veiculo):
    def __init__(self, marca, ano, cilindradas):

        super().__init__(marca, ano)
        self.cilindradas = cilindradas

if __name__ == "__main__":
    meu_carro = Carro("Toyota", 2024, 4)
    minha_moto = Moto("Honda", 2023, 250)

    print("--- Teste Carro ---")
    meu_carro.informacoes()
    print(f"Quantidade de portas: {meu_carro.portas}")

    print("\n--- Teste Moto ---")
    minha_moto.informacoes()
    print(f"Cilindradas: {minha_moto.cilindradas}")