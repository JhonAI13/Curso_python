"""#  Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
a = int(input("Digite um numero."))
b = int(input("Digite um numero."))
c = int(input("Digite um numero."))

if a > b and a > c:
    print("o maior numero é {}".format(a))
if b > a and b > c:
    print("o maior numero é {}".format(b))
if c > a and c > b:
    print("o maior numero é {}".format(c))
if a < b and a < c:
    print("o menor numero é {}".format(a))
if b < a and b < c:
    print("o menor numero é {}".format(b))
if c < a and c < b:
    print("o menor numero é {}".format(c))"""
#  Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
a = int(input("Digite um numero."))
b = int(input("Digite um numero."))
c = int(input("Digite um numero."))

menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print("O menor numero é {}".format(menor))
print("O maior numero é {}".format(maior))


