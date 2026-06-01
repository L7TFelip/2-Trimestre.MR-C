class Pessoa:
	def __init__(self,nome,idade):
		self.__nome = nome
		self.__idade = idade
	def set_nome(self,nome):
		if len(nome) > 0:
			self.__nome = nome
		else:
			print("Nome não pode ser vazio")
	def set_idade(self,idade):
		if 0 <= idade <= 120:
			self.__idade = idade
		else:
			print("Idade deve ser entre 0 e 120")
	def apresentar(self):
		print(f"Olá! Meu nome é {self.__nome}, tenho {self.__idade} anos!")
pessoa1 = Pessoa("Rafael",17)
pessoa1.set_idade(20)
pessoa1.apresentar()
