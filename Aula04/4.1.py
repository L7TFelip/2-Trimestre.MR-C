class Produto:
	def __init__(self, nome, preco):
		self.__nome = nome
		self.__preco = preco
	def get_nome(self):
		return self.__nome
	def get_preco(self):
		return self.__preco
	def set_nome(self,nome):
		if len(nome) > 0:
			self.__nome = nome
		else:
			print("Erro! Nome deve conter carácteres")
	def set_preco(self,preco):
		if preco >= 0:
			self.__preco = preco
		else:
			print("Erro! Preço não pode ser negativo")
p1 = Produto("Televisão",2000.0)
print(p1.get_nome(),p1.get_preco())
p1.set_preco(2500.0)
