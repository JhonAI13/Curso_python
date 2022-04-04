class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print("Inicializando uma conta")
        self.titular = titular
        self.numero = numero
        self.saldo = saldo
        self.limite = limite

    def deposita(self, valor):
        self.saldo += valor

    # def saca(self, valor):
    #     self.saldo -= valor

    def saca(self, valor):
        if (self.saldo < valor):
            return False
        else:
            self.saldo -= valor
            return True

    def extrato(self):
        print(f"numero: {self.numero}\nsaldo: {self.saldo}")

    # def transfere(self, destino, valor):
    #     self.saldo -= valor
    #     destino.saldo += valor

    def transfere_para(self, destino, valor):
        retirou = self.saca(valor)
        if (retirou == False):
            return False
        else:
            destino.deposita(valor)
            return True
