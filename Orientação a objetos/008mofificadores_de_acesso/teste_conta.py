from conta import Conta,Pessoa

minha_conta = Conta('123-4', 'João', 1000.0, 2000.0)
minha_conta.saca(500000)
minha_conta = Conta('123-4', 'João', 1000.0)
minha_conta.saldo = -200
minha_conta = Conta('123-4', 'joão', 1000.0)
novo_saldo = -200
if (novo_saldo < 0):
    print("saldo inválido")
else:
    minha_conta.saldo = novo_saldo

pessoa = Pessoa(20)
# pessoa.idade
print(dir(pessoa))
pessoa.__idade = 25
print(pessoa._Pessoa__idade)
print(dir(pessoa))
"""Parei aqui:
"""