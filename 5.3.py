class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def exibir(self):
        print(f"Funcionário: {self.nome} | Salário Base: R$ {self.salario:.2f}")


class Gerente(Funcionario):
    def __init__(self, nome, salario, bonus):
        super().__init__(nome, salario)
        self.bonus = bonus

    def salario_total(self):
        return self.salario + self.bonus

if __name__ == "__main__":

    gerente_ti = Gerente("Carlos Alberto", 6000.00, 1500.00)
    
    gerente_ti.exibir()
    print(f"Salário Total com Bônus: R$ {gerente_ti.salario_total():.2f}")