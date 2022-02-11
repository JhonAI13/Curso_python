#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
print("Vou dizer se 3 valores formam um circulo. ")
a = int(input("Digite um numero:"))
b = int(input("Digite um numero:"))
c = int(input("Digite um numero:"))

if a + b > c and a + c > b and b + c > a:
    print("Os valores {}cm, {}cm e {}cm, formam um triangulo.".format(a, b, c))
else:
    print("Os valores {}cm, {}cm e {}cm, não formam um triangulo.".format(a, b, c))
