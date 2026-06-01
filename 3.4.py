class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0.0):
        self.titular = titular
        self._saldo = float(saldo_inicial)

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"[Depósito] R${valor:,.2f} adicionado à conta.")
        else:
            print("[Erro] O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if valor <= 0:
            print("[Erro] O valor do saque deve ser positivo.")
        elif valor <= self._saldo:
            self._saldo -= valor
            print(f"[Saque] R${valor:,.2f} realizado com sucesso.")
        else:
            print("[Falha] Saldo insuficiente.")

    def extrato(self):
        print("\n--- EXTRATO BANCÁRIO ---")
        print(f"Titular: {self.titular}")
        print(f"Saldo atual: R${self._saldo:,.2f}")
        print("-------------------------\n")

conta1 = ContaBancaria("Rafael Duclos", 100000000.0)

conta1.depositar(67)
conta1.sacar(50000)
conta1.extrato()
