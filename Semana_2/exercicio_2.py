class Conta:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self._saldo = saldo_inicial

    def depositar(self, valor):
        self._saldo += valor

    def levantar(self, valor):
        if valor <= self._saldo:
            self._saldo -= valor
        else:
            print("Saldo insuficiente!")

    def __str__(self):
        return f"{self._saldo}"
    
c1 = Conta("Ana", 100)
c1.depositar(50)
c1.levantar(30)

print("Saldo final:", c1._saldo)