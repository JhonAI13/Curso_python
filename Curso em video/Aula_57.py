# #  Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# #  Caso esteja errado, peça a digitação novamente até ter um valor correto.
# s = "u"
# while s != "M":
#     s = str(input("Qual seu Sexo:")).upper()
#     if s == 'M':
#         s = 'M'
#         print('M registrado com sucesso')
#     elif s == 'F':
#         s = 'M'
#         print('F registrado com sucesso')
#     else:
#         print('INVALIDO, digite novamente!', end='')

s = str(input("Qual seu Sexo:")).strip().upper()[0]
while s not in "MmFf":
    s = str(input("Dados invalidos. Qual seu Sexo:")).strip().upper()[0]
print('Sexo {} foi registrado'.format(s))
