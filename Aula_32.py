"""# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
print("Irei descobrir se o ano que voce digitar é bicesto ou não")
a = int(input("Digite um ano:"))
if a//4 == a/4:
    if a//100 == a/100:
        a1 = a / 100
        if a1/4 == a1//4:
            print ("Este ano é bicesto!")
        else:
            print("Este ano não é bicesto.")
else:
    print("Este ano não é bicesto.")
"""
# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
import datetime
print("Irei descobrir se o ano que voce digitar é bicesto ou não")
a = int(input("Digite um ano:"))
if a == 0:
    a = datetime.date.today().year
if a//4 == a/4 and a//100 != a/100 or a/400 == a//400:
    print ("{} é bicesto!".format(a))
else:
    print("{} não é bicesto.".format(a))
