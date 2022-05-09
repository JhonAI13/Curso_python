"""096: Faça um programa que tenha uma função chamada área(),
 que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno."""


def area(a, b):
    print(f'A área de um terreno {a} X {b} é de {a * b}m².')


a = float(input('LARGURA (M): '))
b = float(input('COMPRIMENTO (M): '))
area(a, b)

