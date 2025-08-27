class ContaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0

    def deposito(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor

    def exibir_saldo(self):
        print(f"{self.titular} seu saldo é {self.saldo}")


conta = ContaBancaria("João")
conta.deposito(500)
conta.sacar(100)
conta.exibir_saldo()