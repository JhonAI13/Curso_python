class Conta:
    def	__init__(self, numero, titular, saldo, limite):
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


    def	deposita(self,	valor):
        """Soma um valor a conta

        Args:
            conta (_type_): numero da conta
            valor (_type_): quantidade a ser somada a conta
        """
        self.saldo	+=	valor

    # def	saca(self,	valor):
    #     """subtrai o valor da conta.

    #     Args:
    #         conta (_type_): A conta cadastrada
    #         valor (_type_): O valor a ser sacado
    #     """
    #     self.saldo	-=	valor

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
            return True
    def transfere(self, destino, valor):
        retirou = self.sacar(valor)
        if (retirou == False):
            return False
        else:
            destino.deposita(valor)
            return True
