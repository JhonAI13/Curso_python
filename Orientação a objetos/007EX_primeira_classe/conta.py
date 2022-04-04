import datetime


class Historico:

    def __init__(self):
        self.data_abertura = datetime.datetime.today()
        self.transacoes = []

    def imprime(self):
        print(f"data abertura: {self.data_abertura}")
        print(f"transações do(a) : ")
        for t in self.transacoes:
            print("-", t)


class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf


class Conta:
    def __init__(self, numero, cliente, saldo, limite=1000.0):
        print("Inicializando uma conta")
        self.titular = cliente
        self.numero = numero
        self.saldo = saldo
        self.limite = limite
        self.historico = Historico()

    def deposita(self, valor):
        self.saldo += valor
        self.historico.transacoes.append(f"depósito de {valor}")

    def saca(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            self.historico.transacoes.append(f"saque de {valor}")

    def extrato(self):
        print(f"numero: {self.numero}\nsaldo: {self.saldo}")
        self.historico.transacoes.append(f"tirou extrato - saldo de {self.saldo}")

    def transfere_para(self, destino, valor):
        retirou = self.saca(valor)
        if (retirou == False):
            return False
        else:
            destino.deposita(valor)
            self.historico.transacoes.append(f"transferencia de {valor} para conta {destino.numero}")
            return True
