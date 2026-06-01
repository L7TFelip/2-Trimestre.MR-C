class ContaBancaria():
	def __init__(self,titular,saldo):
		self.__titular = titular
		self.__saldo = saldo
	def depositar(self,valor):
		if valor > 0:
			self.__saldo+=valor
		else:
			("Erro: Digite apenas valores positivos")
	def sacar(self,valor):
		if self.__saldo >= valor:
			self.__saldo -= valor
		else:
			print("Erro: Saldo insuficiente")
	def get_saldo(self):
		return self.__saldo
	def extrato(self):
		print(f"Titular: {self.__titular} | Saldo: {self.__saldo}")
conta1 = ContaBancaria("Rafael Duclos",1000.0)
conta1.depositar(500.0)
conta1.sacar(250.0)
print(conta1.get_saldo())
conta1.extrato()
