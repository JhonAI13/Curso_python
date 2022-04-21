# # 080 -Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# # já na posição correta de inserção sem usar o sort(). no final, mostre a lista ordenada na tela.
# l = []
# for x in range(0, 5):
#     l.insert(x, int(input('Digite o numero:')))
#     if x != 0:
#         for v in range(0, len(l)):
#             if l[x] < l[v]:
#                 l.insert(v, l[x])
#                 l.pop()
#                 break
#         if v == len(l) - 1:
#             print('Adicionado ao final da lista...')
#         else:
#             print(f"Adicionado na posição {v} da lista...")
#     else:
#         print('Adicionado ao final da lista...')
# print('=-'* 40)
# print(f'Os valores digitados em ordem foram{l}')

l = []
for x in range(0, 5):
    n = int(input('Digite um valor'))
                        # para ver o ultimo elemento da lista
    if x == 0 or n > l[-1]:
    #elif n > l[-1]:
        l.append(n)
        print('Adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(l):
            if n <= l[pos]:
                l.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista')
                break
            pos += 1
print('=-'* 40)
print(f'Os valores digitados em ordem foram{l}')
