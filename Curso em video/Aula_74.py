# # Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# #Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
# import random
# p = random.sample([1, 2, 3, 4, 5, 6, 7, 8, 9], k=5)
# print(f'Os valores sorteados são:{p}')
# ma = me = 0
# for c in range (5):
#     if c == 0:
#         me = p[c]
#         ma = p[c]
#     else:
#         if p[c] > ma:
#             ma = p[c]
#         elif p[c] < me:
#             me = p[c]
# print(f'''O maior valor foi:{ma}
# O menor valor foi:{me}''')

import random
p = random.sample([1, 2, 3, 4, 5, 6, 7, 8, 9],k=5)
print(f'Os valores sorteados são:{p}')
print(f'''O maior valor foi:{max(p)}
O menor valor foi:{min(p)}''')
