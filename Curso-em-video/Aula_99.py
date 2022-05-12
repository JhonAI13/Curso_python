# """99: Faça um programa que tenha uma função chamada maior(),
# que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior."""
#
# from time import sleep
#
#
# def analize(*num):
#     print('-=~' * 20)
#     print(f'Analizando os calores passados...')
#     sleep(0.5)
#     ma = 0
#     if num == ():
#         print(f'Foram informados 0 valores ao todo.')
#         print(f'O maior valor informado foi 0')
#     for x in range(0, len(num)):
#         print(num[x], end=' ')
#         if x == 0:
#             ma = num[x]
#         else:
#             if num[x] > ma:
#                 ma = num[x]
#         if x == len(num) - 1:
#             print(f'Foram informados {len(num)} valores ao todo.')
#             print(f'O maior valor informado foi {ma}')
#
#
# analize(2, 9, 7, 6, 4, 6, 7)
# analize(5, 3, 4, 5, 6)
# analize(12, 4, 56)
# analize()

"""99: Faça um programa que tenha uma função chamada maior(),
que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior."""

from time import sleep


def analize(*num):
    print('-=~' * 20)
    print(f'Analizando os calores passados...')
    sleep(0.5)
    ma = cont = 0
    for v in num:
        print(f'{v}', end=' ')
        if cont == 0:
            ma = v
        else:
            if v > ma:
                ma = ma
        cont += 1
    print(f'''Foram informados {cont} valores ao todo.
O maior valor informado foi {ma}.''')


analize(2, 9, 7, 6, 4, 6, 7)
analize(5, 3, 4, 5, 6)
analize(12, 4, 56)
analize()

