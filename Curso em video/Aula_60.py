# #Faça um programa que leia um número qualquer e mostre o seu fatorial.Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
# n = int(input('Digite o numero a ser fatorado:'))
# c = n
# print('{}!'.format(n), "=", end='')
# for x in range(n-1):
#     c -= 1
#     n = n * c
#     print(' {} '.format(c), end='')
#     if c != 1:
#         print('X', end='')
#     if c == 1:
#         print('=', n)

n = int(input('Digite o numero a ser fatorado:'))
c = n
f = 1
print('{}! = '.format(n), end='')
while c > 1:
    print(c, end='')
    print(' x 'if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print("=", f, end='')
