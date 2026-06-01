class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula

    def apresentar(self):
        print(f"[ALUNO] Nome: {self.nome} | Idade: {self.idade} anos | Matrícula: {self.matricula}")


class Professor(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario

    def apresentar(self):
        print(f"[PROFESSOR] Nome: {self.nome} | Idade: {self.idade} anos | Salário: R$ {self.salario:.2f}")

if __name__ == "__main__":

    lista_pessoas = [
        Aluno("Bruno", 20, "20260102"),
        Professor("Helena", 45, 5500.00),
        Aluno("Mariana", 22, "20260105"),
        Professor("Cláudio", 38, 6200.00)
    ]

    print("--- Apresentação dos Integrantes ---")

    for pessoa in lista_pessoas:
        pessoa.apresentar()