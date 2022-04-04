from conta import Conta
def cria_conta(numero, tirular, saldo, limite):
    """
    Cria uma conta apos dados os dados:
    :param numero: numero da conta
    :param tirular: nome do titular
    :param saldo: Valor da conta
    :param limite: limite de dinheiro a ser gasto
    :return: retorna um dicionario com estes dados organizados
    """
    conta = {"numero":numero, "titular":tirular, "saldo":saldo, "limite":limite}
    return conta


def deposita(conta,valor):
    """
    Realiza a soma do deposito na conta
    :param conta: dicionario do criar_conta
    :param valor: Valor a ser somado
    :return: Retorna a lista com o valor somado
    """
    conta["saldo"] +=valor


def saca(conta, valor):
    """
    Realiza a subitração do saque  na conta
    :param conta: dicionario do criar_conta
    :param valor: Valor a ser subitraido
    :return: Retorna a lista com o valor somado
    """
    conta["saldo"] -= valor


def extrato(conta):
    """
    Printa o numero e o saldo do dicionario
    :param conta: o dicionario de criar_conta
    :return: Printa o numero e o saldo do dicionario
    """
    print(f"numero: {conta['numero']} \nsaldo: {conta['saldo']}")


# conta = cria_conta('123-7', 'João', 500.0, 1000.0)
# deposita(conta, 50.0)
# extrato(conta)
#
# saca(conta, 20.0)
# extrato(conta)

# conta = Conta()
# print(type(conta))
#
# conta.titular = "João"
# print(conta.titular)
# conta.saldo = 120.0
# print(conta.saldo)

conta = Conta('123-4', 'João', 120.0, 1000.0)
print(conta.titular)
print(conta.saldo)

"""Parei aqui:
Discuta com seus colegas e instrutor as vantagens da orientação a objetos até aqui."""