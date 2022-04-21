# #  Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
# #  Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites
# #  foram necessários para vencer.
# import random
# n = random.randrange(1,11)
# t = int(input('Digite seu chute: '))
# c = 1
# while n != t:
#     c += 1
#     if n != t:
#         print('Você errou!')
#     if n > t:
#         print('Mais...')
#     elif n < t:
#         print('Menos...')
#     t = int(input('Digite novamente, seu chute'))
# print('Você precisou de {} tentativas para acertar.'.format(c))

import random
n = random.randrange(1, 11)
a = False
c = 1
while not a:
    c += 1
    t = int(input('Digite novamente, seu chute: '))
    if t == n:
        a = True
    if n != t:
        print('Você errou!')
    if n > t:
        print('Mais...')
    elif n < t:
        print('Menos...')
print('Você precisou de {} tentativas para acertar.'.format(c))
