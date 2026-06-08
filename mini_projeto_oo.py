#Classe Mãe
class Funcionario:
    def __init__(self, nome, matricula, salario_fixo):
        self._nome = nome
        self._matricula = matricula
        self.set_salario(salario_fixo)

    def get_nome(self):
        return self._nome

    def get_matricula(self):
        return self._matricula

    def get_salario(self):
        return self._salario_fixo
    
    def set_salario(self, valor):
        if valor < 0:
            print("Erro: O salário não pode ser negativo! Definido como 0.")
            self._salario_fixo = 0
        else:
            self._salario_fixo = valor


#Classes Filhas

class CLT(Funcionario):
    def calcular_salario(self):
        return self.get_salario()

    def exibir(self):
        print(f"Nome : {self.get_nome()} | Matricula : {self.get_matricula()} | Tipo : CLT | Salario : R$ {self.calcular_salario():.2f}")


class Vendedor(Funcionario):
    def __init__(self, nome, matricula, salario_fixo, total_vendas):
        super().__init__(nome, matricula, salario_fixo)
        self.total_vendas = total_vendas

    def calcular_salario(self):
        return self.get_salario() + (self.total_vendas * 0.10)

    def exibir(self):
        print(f"Nome : {self.get_nome()} | Matricula : {self.get_matricula()} | Tipo : Vendedor | Salario : R$ {self.calcular_salario():.2f}")


class Gerente(Funcionario):
    def calcular_salario(self):
        return self.get_salario() + 1500.00

    def exibir(self):
        print(f"Nome : {self.get_nome()} | Matricula : {self.get_matricula()} | Tipo : Gerente | Salario : R$ {self.calcular_salario():.2f}")


#Programa Principal
lista_funcionarios = []

print("CADASTRO DE FUNCIONÁRIOS")

#Cadastro de 3 funcionários
for i in range(3):
    print(f"\nCadastro do {i+1}º Funcionário")
    nome = input("Nome: ")
    matricula = input("Matrícula: ")
    salario = float(input("Salário Fixo: R$ "))
    
    print("Escolha o tipo: [1] CLT [2] Vendedor [3] Gerente")
    opcao = input("Opção: ")

    if opcao == "1":
        novo_func = CLT(nome, matricula, salario)
    elif opcao == "2":
        vendas = float(input("Total de vendas realizadas: R$ "))
        novo_func = Vendedor(nome, matricula, salario, vendas)
    elif opcao == "3":
        novo_func = Gerente(nome, matricula, salario)
    else:
        print("Opção inválida! Cadastrado como CLT por padrão.")
        novo_func = CLT(nome, matricula, salario)

    lista_funcionarios.append(novo_func)

#Exibição final dos resultados
print("           Folha pagamento RH")
for f in lista_funcionarios:
    f.exibir()

print("Mr - C")