from conta import Conta

# conta = Conta('123-4', 'João', 120.0, 1000.0)
# conta.deposita(20.0)
# conta.extrato()
#
# print()
#
# conta.saca(15)
# conta.extrato()
#
# print()
#
# conta.saldo = 1000
# if (conta.saca(2000)):
#     print('consegui sacar')
# else:
#     print('não consegui sacar')
#
# print()
#
# c1 = Conta('123-4', 'João', 120.0, 1000.0)
# c2 = c1
# print(c2.saldo)
#
# c1.deposita(100.0)
# print(c1.saldo)
#
# c2.deposita(30.0)
# print(c2.saldo)
#
# print(c1.saldo)
#
# print()
#
# print(id(c1))
# print(id(c2))
#
# print(id(c1) == id(c2))
#
# print()

c1 = Conta("123-4", "Python", 500.0, 1000.0)
c2 = Conta("321-4", "Python", 900.0, 1000.0)
if c1 == c2:
    print("contas iguais")
else:
    print("contas opostas")

c1.extrato()
c2.extrato()

print()
if c1.transfere_para(c2, 20):
    print("Transferimento efetuado")
else:
    print("Não possue saldo")

c1.extrato()
c2.extrato()
"""Parei aqui:
A leitura deste código seria "conta1 transfere para conta2 50 reais". """