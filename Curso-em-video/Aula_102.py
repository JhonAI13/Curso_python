# """ 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
#  o primeiro que indique o número a calcular e outro chamado show, que será um valor
#   lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial."""
#
#
# def fatorial(n, show=False):
#     """
#     -> e uma função que dis a fatorial.
#     :param n: o numero a fatorar
#     :param show: Se você quer que apareça o historico
#     :return: sem retorno
#     """
#     c = n
#     if show:
#         print('{}!'.format(c), "=", end='')
#         print(' {}'.format(c), 'X', end='')
#     for x in range(n - 1):
#         c -= 1
#         n = n * c
#         if show:
#             print(' {} '.format(c), end='')
#             if c != 1:
#                 print('X', end='')
#             if c == 1:
#                 print('=', end='')
#     print(n)
#
#
# fatorial(6, show=True)
# fatorial(8)
# help(fatorial)
#
""" 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
 o primeiro que indique o número a calcular e outro chamado show, que será um valor
  lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial."""


def fatorial(n, show=False):
    """
    -> e uma função que dis a fatorial.
    :param n: o numero a fatorar
    :param show: Se você quer que apareça o historico
    :return: sem retorno
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f



print(fatorial(5, show=True))
print(fatorial(6))
help(fatorial)

