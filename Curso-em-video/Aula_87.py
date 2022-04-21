# #  087: Aprimore o desafio anterior, mostrando no final:
# # A) A soma de todos os valores pares digitados.
# # B) A soma dos valores da terceira coluna.
# # C) O maior valor da segunda linha.
# l = [[], [], [], [], [], [], [], [], []]
# f = ''
# s = v3 = m3 = 0
# for x in range(0, 9):
#     l[x].append(int(input('Digite um numero:')))
# print('-=' * 30)
# for c in range(0, 9, 3):
#     if c != 0:
#         f = '\n'
#     print(f, f'[{l[c][0]:^5}]', f'[{l[c+1][0]:^5}]', f'[{l[c+2][0]:^5}]', end='')
# print('\n', '-=' * 30)
# for x in range(0, 9):
#     if l[x][0] / 2 == l[x][0] // 2:
#         s += l[x][0]
#     if x in (6, 7, 8):
#         v3 += l[x][0]
#     if x in (1, 4, 7):
#         if x == 7:
#             m3 = l[x][0]
#         elif l[x][0] > m3:
#             m3 = l[x][0]
#
# print(f'''A soma dos valores pares é {s}
# A soma dos valores da terceira coluna é:{v3}
# O maior valor da segunda linha é :{m3}''')

l = [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]
s = v3 = m3 = 0
for x in range(0, 3):
    for c in range(0, 3):
        l[x][c] = int(input(f'Digite um valor para [{x}, {c}]:'))
print('-=' * 30)
for x in range(0, 3):
    for c in range(0, 3):
        print(f'[{l[x][c]:^5}]', end='')
        if l[x][c] % 2 == 0:
            s += l[x][c]
    print()
for x in range (0, 3):
    v3 += l[x][2]
    if c == 0:
        m3 = l[1][x]
    elif l[1][x] > m3:
        m3 = l[1][x]
print('-=' * 30)
print(f'''A soma dos valores pares é {s}
A soma dos valores da terceira coluna é:{v3}
O maior valor da segunda linha é :{m3}''')
