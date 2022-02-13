#  Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor
#  digitado for ímpar, desconsidere-o.
t = 0
for c in range(0,6):
    n = int(input('Digite um numero:'))
    if n / 2 == n // 2:
        t = n + t
print(t)
