# # Crie um programa que leia vários números inteiros pelo teclado.
# # O programa só vai parar quando o usuário digitar o valor 999,
# # que é a condição de parada. No final, mostre quantos números
# # foram digitados e qual foi a soma entre eles (desconsiderando o flag).
# x = 0
# y = 0
# c = 0
# while x != 999:
#     x = int(input('Digite um número[999 para parar:' ))
#     if x != 999:
#         y = x + y
#         c += 1
# print('Você digitou {} numeros e a soma é {}'.format(c, y))

x = y = c = 0
x = int(input('Digite um número[999 para parar:' ))
while x != 999:
    y = x + y
    c += 1
    x = int(input('Digite um número[999 para parar:' ))
print('Você digitou {} numeros e a soma é {}'.format(c, y))
