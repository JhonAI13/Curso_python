# # 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# # A) Quantas pessoas foram cadastradas.
# # B) Uma listagem com as pessoas mais pesadas.
# # C) Uma listagem com as pessoas mais leves.
# d = []
# g = []
# f = ma = me = 0
# while True:
#     g.append(str(input('Qual nome: ')))
#     g.append(float(input('Qual a peso:')))
#     d.append(g[:])
#     g.clear()
#     f += 1
#     c = str(input('Você quer continuar[S/N]?:')).strip().upper()
#     while c not in "SsNn":
#         c = str(input("""Dados invalidos....
#     	Você quer continuar[S/N]?:""")).strip().upper()
#     if c in 'Nn':
#         break
#
# for x in range(0, len(d)):
#     if x == 0:
#         ma = me = d[x][1]
#     else:
#         if d[x][1] > ma:
#             ma = d[x][1]
#         if d[x][1] < me:
#             me = d[x][1]
# mal = []
# mel = []
# for x in range(0, len(d)):
#     if ma == d[x][1]:
#         mal.append(d[x][0])
#     if me == d[x][1]:
#         mel.append(d[x][0])
# print(f'''Tem {f} pessoas na lista.
# O maior peso foi de {ma:.1f}Kg Peso de {mal}
# O menor peso foi de {me:.1f}Kg Peso de {mel}  ''')

d = []
g = []
ma = me = 0
while True:
    g.append(str(input('Qual nome: ')))
    g.append(float(input('Qual a peso:')))
    if len(d) == 0:
        ma = me = g[1]
    else:
        if g[1] > ma:
            ma = g[1]
        if g[1] < me:
            me = g[1]
    d.append(g[:])
    g.clear()
    c = str(input('Você quer continuar[S/N]?:')).strip().upper()
    while c not in "SsNn":
        c = str(input("""Dados invalidos....
        Você quer continuar[S/N]?:""")).strip().upper()
    if c in 'Nn':
        break
print(f'''Tem {len(d)} pessoas na lista.
O maior peso foi de {ma:.1f}Kg Peso de: ''', end='')
for x in d:
    if x[1] == ma:
        print(f'{x[0]} ', end='')
print(f'\nO maior peso foi de {me:.1f}Kg Peso de: ', end='')
for x in d:
    if x[1] == me:
        print(f'{x[0]} ', end='')
print()
