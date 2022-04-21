#   070: Crie um programa que leia o nome e o preço de vários produtos.
#   O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.
A = B = r = 0
c = C = ''
me = 2 ** 10
print('~^'*50)
while True:
    s = str(input("Nome do produto:"))
    n = float(input('Qual o valor:'))
    r += 1
    #Calculos estatisticos
    if n < me:
        me = n
        C = s
    A = A + n
    if n > 1000:
        B += 1
    c = str(input('Você quer continuar[S/N]?:')).strip().upper()[0]
    while c not in "SsNn":
        c = str(input("""Dados invalidos.
Você quer continuar[S/N]?:""")).strip().upper()[0]
    print('~^' * 50)
    if c in 'Nn':
        break
print(f'''O total gasto na compra R${A}0.
Tem {B} produtos custam mais de R$1000,00.
O nome do produto mais barato é {C} que custa R${me}0. ''')
print('~^'*50)
