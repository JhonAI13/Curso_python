from conta import Conta, Cliente

# conta = Conta('123-4', 'joão', 120.0)
# print(conta.limite)

print()

cliente = Cliente('João', 'Oliveira', '1111111111-1')
minha_conta = Conta('123-4', cliente, 120.0, 1000.0)

print(minha_conta.titular)
print(minha_conta.titular.nome)

print("\nTudo é class!")
print(type(minha_conta.numero))
print(type(minha_conta.saldo))
print(type(minha_conta.titular))

"""Parei aqui:
"""