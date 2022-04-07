# # Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# #A) Quantas vezes apareceu o valor 9.
# #B) Em que posição foi digitado o primeiro valor 3.
# #C) Quais foram os números pares.
# p = (int(input('Digite um numero')),
#      int(input('Digite outro numero')),
#      int(input('Digite mais um numero')),
#      int(input('Digite o último numero')))
# v = v2 = x = f = 0
# for c in range(4):
#     if p[c] == 9:
#         v += 1
# for c in range(4):
#     if p[c] == 3:
#         v2 = c
#         break
# for c in range(4):
#     if p[c]//2 == p[c]/2:
#         x = f'{p[c]}'
# print(f'''{p}
# O valor 9 apareceu {v} vezes.
# O valor 3 apareceu na {v2+1}ª posição.
# Os valores pares digitados foram:{x}''')

p = (int(input('Digite um numero')),
     int(input('Digite outro numero')),
     int(input('Digite mais um numero')),
     int(input('Digite o último numero')))
print(f'''{p}
O valor 9 apareceu {p.count(9)} vezes.''')
if 3 in p:
    print(f'O valor 3 apareceu na {p.index(3)+1}ª posição.')
else:
    print('O numero 3 não foi digitado')
print('Os valores pares digitados foram:', end='')
for c in range(4):
    if p[c]//2 == p[c]/2:
        print(p[c], end=' ')
