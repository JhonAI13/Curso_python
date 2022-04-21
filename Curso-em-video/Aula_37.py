# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher
# qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

n = int(input('Digite um numero:'))
print('Qual converssão quer fazer?')
c = int(input('1 para binário, 2 para octal e 3 para hexadecimal:'))
if c == 1:
    d1 = n // 2
    d2 = d1 // 2
    d3 = d2 // 2
    d4 = d3 // 2
    d5 = d4 // 2
    d6 = d5 // 2
    d7 = d6 // 2
    d8 = d7 // 2
    n1 = n % 2
    n2 = d1 % 2
    n3 = d2 % 2
    n4 = d3 % 2
    n5 = d4 % 2
    n6 = d5 % 2
    n7 = d6 % 2
    n8 = d7 % 2
    print('Seu numero em decimal é:{}{}{}{}{}{}{}{}'.format(n8,n7, n6, n5, n4, n3, n2, n1))
elif c == 2:
    d1 = n // 8
    d2 = d1 // 8
    d3 = d2 // 8
    d4 = d3 // 8
    d5 = d4 // 8
    d6 = d5 // 8
    d7 = d6 // 8
    d8 = d7 // 8
    n1 = n % 8
    n2 = d1 % 8
    n3 = d2 % 8
    n4 = d3 % 8
    n5 = d4 % 8
    n6 = d5 % 8
    n7 = d6 % 8
    n8 = d7 % 8
    print('Seu numero em octal é:{}{}{}{}{}{}{}{}'.format(n8, n7, n6, n5, n4, n3, n2, n1))
elif c == 3:
   print('Seu numero em hexadecimal12412 é:{}'.format(hex(n)))
