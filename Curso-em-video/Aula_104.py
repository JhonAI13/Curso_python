# """ 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma
# semelhante 'a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
# Ex: n = leiaInt('Digite um n: ')"""
#
#
# def leia_int(num):
#     n = str(input(num))
#     while True:
#         if not n.isnumeric():
#             print('Erro! digite um numero valido')
#             n = str(input(num))
#         else:
#             break
#     return n
#
#
# n = leia_int('Difite um numero:')
# print(f'Você acabou de digitar o numero {n}')

def leia_int(num):
    n = str(input(num))
    while True:
        if not n.isnumeric():
            print('\033[31mERRO! Digite um número inteiro válido\033[m')
            n = str(input(num))
        else:
            break
    return n


n = leia_int('Difite um numero:')
print(f'Você acabou de digitar o numero {n}')
