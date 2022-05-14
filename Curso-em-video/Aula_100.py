# """100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia()
#  e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a
#  segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior."""
# from random import randrange
#
#
# def sorteando(num):
#     for c in range(0, 5):
#         num.append(randrange(10))
#
#
# def somando_pares(num):
#     soma = 0
#     for v in range(0, len(num)):
#         if num[v] / 2 == num[v] // 2:
#             soma += num[v]
#     return soma
#
#
# num = list()
# sorteando(num)
# print(f'''Sorteando 5 alores da lista:{num}
# Somando os valores pares de {num}, temos {somando_pares(num)}''')

"""100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia()
 e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a
 segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior."""
from random import randrange


def sorteando(num):
    print('Soteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        n = randrange(10)
        num.append(n)
        print(f'{n} ', end=' ')
    print('Pronto!')


def somando_pares(num):
    soma = 0
    for v in range(0, len(num)):
        if num[v] / 2 == num[v] // 2:
            soma += num[v]
    print(f'Somando os valores pares de {num}, temos {soma}.')


num = list()
sorteando(num)
somando_pares(num)
