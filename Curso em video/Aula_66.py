# Crie um programa que leia vários números inteiros pelo teclado. O programa
# so vai para quando o usuario digitar o valor 999, que e a condição de parada.
# No final mostre quantos numeros foram digitados e qual foi a soma entre eles(desconsiderando o flag)
c = y = 0
while True:
    x = int(input('Digite um numero:'))
    if x == 999:
        break
    y += x
    c += 1
print(f'Foram digitados {c} numeros. E a soma entre eles é {y}')
