class ContaBancaria:
    def __init__(self):
        self.saldo = 0
        self.saques_realizados = []
        self.depositos_realizados = []

    def deposito(self, valor):
        self.saldo += valor
        self.depositos_realizados.append(valor)
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")

    def saque(self, valor):
        if self.saldo >= valor and len(self.saques_realizados) < 3 and valor <= 500:
            self.saldo -= valor
            self.saques_realizados.append(valor)
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        elif valor > 500:
            print("Limite máximo por saque é de R$ 500.00.")
        elif len(self.saques_realizados) >= 3:
            print("Limite máximo de saques diários atingido.")
        else:
            print("Saldo insuficiente para realizar o saque.")

    def extrato(self):
        print("\nExtrato:")
        print("Depósitos realizados:")
        for deposito in self.depositos_realizados:
            print(f"- R$ {deposito:.2f}")
        print("\nSaques realizados:")
        for saque in self.saques_realizados:
            print(f"- R$ {saque:.2f}")
        print(f"\nSaldo atual: R$ {self.saldo:.2f}")


# Teste do sistema bancário
conta = ContaBancaria()
conta.deposito(1000)
conta.saque(500)
conta.saque(300)
conta.saque(200)
conta.saque(600)
conta.extrato()
