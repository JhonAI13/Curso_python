# #  086: Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
# #  No final, mostre a matriz na tela, com a formatação correta.
# l = [[], [], [], [], [], [], [], [], []]
# f = ''
# for x in range(0, 9):
#     l[x].append(int(input('Digite um numero:')))
# for c in range(0, 9, 3):
#     if c != 0:
#         f = '\n'
#     print(f, f'[{l[c][0]:^3}]', f'[{l[c+1][0]:^3}]', f'[{l[c+2][0]:^3}]', end='')

l = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for x in range(0, 3):
    for c in range(0, 3):
        l[x][c] = int(input(f'Digite um valor para [{x}, {c}]:'))
print('-=' * 30)
for x in range(0, 3):
    for c in range(0, 3):
        print(f'[{l[x][c]:^5}]', end='')
    print()
