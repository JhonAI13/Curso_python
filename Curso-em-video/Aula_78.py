# #078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final,
# #mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
# l = [int(input('Digite o numero:')),
# int(input('Digite o numero:')),
# int(input('Digite o numero:')),
# int(input('Digite o numero:')),
# int(input('Digite o numero:'))]
# ma = me =  0
# for c, v in enumerate(l):
#     if c == 0:
#         ma = v
#         me = v
#     else:
#         if v > ma:
#             ma = v
#         if v < me:
#             me = v
# print(f'O maior numero {ma}, sua posição é: ', end='')
# for c, v in enumerate(l):
#     if v == ma:
#         print(c+1, end=" ")
# print('')
# print(f'O menor numero {me}, sua posição é: ', end='')
# for c, v in enumerate(l):
#     if v == me:
#         print(c+1, end=" ")

l = []
ma = me = 0
for c in range(0, 5):
    l.append(int(input('Digite o numero:')))
    if c == 0:
        ma = l[c]
        me = l[c]
    else:
        if l[c] > ma:
            ma = l[c]
        if l[c] < me:
            me = l[c]
print(f'O maior numero {ma}, sua posição é: ', end='')
for c, v in enumerate(l):
    if v == ma:
        print(c+1, end=" ")
print()
print(f'O menor numero {me}, sua posição é: ', end='')
for c, v in enumerate(l):
    if v == me:
        print(c+1, end=" ")
