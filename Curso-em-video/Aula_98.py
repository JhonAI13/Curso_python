# """98: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
#
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada"""
# from time import sleep
#
#
# def contagem(a, b, c):
#     print('-=~'*20)
#     print(f'Contagem de {a} até {b} de {c} em {+c}')
#     if c == 0:
#         if a > b:
#             c = -1
#         elif a < b:
#             c = +1
#     elif a > b and c > 0:
#         c = -c
#         b = b - 1
#     elif a < b and c < 0:
#         c = +c
#         b = b + 1
#     if c < 0:
#         b -= 1
#     if c > 0:
#         b += 1
#     for c in range(a, b, c):
#         print(c, end=' ')
#         sleep(0.3)
#     print('Fim!')
#
#
# contagem(1, 10, 0)
# contagem(10, 0, 2)
# inicio = int(input("Início: "))
# fim = int(input("Fim: "))
# passo = int(input("Passo: "))
# contagem(inicio, fim, passo)

from time import sleep


def contagem(a, b, c):
    if c < 0:
        c += -1
    if c == 0:
        c = 1
    print('-=~' * 20)
    print(f'Contagem de {a} até {b} de {c} em {c}.')

    if a < b:
        cont = a
        while cont <= b:
            print(f'{cont}', end=' ')
            cont += c
            sleep(0.2)
        print('FIM!')
    else:
        cont = a
        while cont >= b:
            print(f'{cont}', end=' ')
            cont -= c
            sleep(0.2)
        print('FIM')


contagem(1, 10, 0)
contagem(10, 0, 2)
inicio = int(input("Início: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))
contagem(inicio, fim, passo)

