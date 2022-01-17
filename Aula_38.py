#Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#- O primeiro valor é maior
#- O segundo valor é maior
#- Não existe valor maior, os dois são iguais

n1 = int(input("Digite o primeiro numero:"))
n2 = int(input("Digite o segunto numero:"))

if n1 > n2:
    print("O primeiro valor é o maior")
elif n2 > n1:
    print("O segundo valor é o maior.")
elif n1 == n2:
    print("Os dois valores são iguais")
