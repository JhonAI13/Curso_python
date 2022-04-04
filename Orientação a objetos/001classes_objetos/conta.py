# class Conta:
#     pass


class Conta:
    def __init__(self, numero,titular , saldo, limiete):
        print("Inicializando uma conta")
        self.titular = titular
        self.numero = numero
        self.saldo = saldo
        self.limite = limiete

