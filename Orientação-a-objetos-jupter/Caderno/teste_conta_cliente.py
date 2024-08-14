from datetime import datetime

class Cliente:
    def __init__(self, nome, sobrenome, cpf):
         self.nome = nome
         self.sobrenome = sobrenome
         self.cpf = cpf
         print("Cliente cadastrado.")

class Historico:
    def __init__(self):
        self.data_abertura = datetime.today()
        self.transacoes = []

    def imprime(self):
        print("data abertura: {}". format(self.data_abertura))
        print("transações: ")
        for t in self.transacoes:
            print("-", t)

class Conta:
    def	__init__(self, numero, titular, saldo, limite=1000):
        """cria uma conta

        Args:
        numero (_type_): numero de identificação da conta
        titular (_type_): nome do titular
        saldo (_type_): quantidade de dinhiro que tem na conta
        limite (_type_): _description_
        """ 
        print("inicializando uma conta")
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.historico = Historico()

    def	deposita(self,	valor):
        """Soma um valor a conta

        Args:
            conta (_type_): numero da conta
            valor (_type_): quantidade a ser somada a conta
        """
        self.saldo	+=	valor
        self.historico.transacoes.append("+{}".format(valor)) 

    def	extrato(self):
        """Dis quanto tem na conta

        Args:
            conta (_type_): numero da conta
        """
        print("numero: {} \nsaldo: {}".format(self.numero, self.saldo))

    def saca(self, valor):
        if (self.saldo < valor):
            return False
        else:
            self.saldo	-=	valor
            self.historico.transacoes.append("-{}".format(valor)) 
            return True
    
    def transfere(self, destino, valor):
        retirou = self.saca(valor)
        if (retirou == False):
            return False
        else:
            destino.deposita(valor)
            self.historico.transacoes.append("transferencia de {} para conta{}".format(valor, destino.numero))
            return True
