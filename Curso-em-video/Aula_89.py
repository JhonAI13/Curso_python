# '''089: Crie um programa que leia nome e duas notas devários alunos
#  e guarde tudo em uma lista composta. No final, mostre um boletim
#  contendo a média de cada um e permita que o usuário possa mostrar
#  as notas de cada aluno individualmente.'''
#
# l = [[]]
# p = []
# c = 0
# while True:
#     p.append(str(input('Nome:')))
#     p.append(float(input('Nota 1:')))
#     p.append(float(input('Nota 2:')))
#     l.append(p[:])
#     p.clear()
#     c = str(input('Você quer continuar[S/N]?:')).strip().upper()
#     while c not in "SsNn":
#         c = str(input("""Dados invalidos....
# Você quer continuar[S/N]?:""")).strip().upper()
#     if c in 'Nn':
#         break
#
# print('=-' * 13)
# print('''No. Nome           Média''')
# print('=-' * 13)
# for c in range(1, len(l)):
#     print(c, f'  {l[c][0]:<14}', f'{(l[c][2] + l[c][1]) / 2 :>5}')
# print('=-' * 13)
# while True:
#     x = int(input('Mostrar notas de qual aluno?(999 interrompe):'))
#     if x == 999:
#         break
#     else:
#         print(f'Notas de {l[x][0]} são {l[x][1], l[x][2]}')
#

ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')
print('-=' * 30)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< VOLTE SEMPRE >>>')

