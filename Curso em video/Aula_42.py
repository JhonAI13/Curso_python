#Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#- EQUILÁTERO: todos os lados iguais
#- ISÓSCELES: dois lados iguais, um diferente
#- ESCALENO: todos os lados diferentes
print("Vou dizer se 3 valores formam um circulo. ")
print("E que tipo de de trianculo é.")
a = int(input("Digite um numero:"))
b = int(input("Digite um numero:"))
c = int(input("Digite um numero:"))

if a + b > c and a + c > b and b + c > a:
    print("Os valores {}cm, {}cm e {}cm, formam um triangulo.".format(a, b, c))
    if a == b and a == c and c == b:
        print('EQUILÁTERO')
    elif a == b or b == a or c == a or c == b:
        print('ISÓSCELES')
    else:
        print('ESCALENO')
else:
    print("Os valores {}cm, {}cm e {}cm, não formam um triangulo.".format(a, b, c))
