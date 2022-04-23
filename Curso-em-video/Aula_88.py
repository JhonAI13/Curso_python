# """088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números
# entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.."""
# print('-=' * 30)
# print('{:^60}'.format('JOGO DA MEGA SENA'))
# print('-=' * 30)
# import random
# import time
#
# um_a_sessenta = []
# for c in range(0, 60):
#     um_a_sessenta.append(c + 1)
# jogo = list()
# numero_sorteio = int(input('Quantos jogos você quer que eu sorteie?'))
# for c in range(0, numero_sorteio):
#     jogo.append(random.sample(um_a_sessenta, k=6)[:])
#     print(f'Jogo {c + 1}:{sorted(jogo[c])}')
#     time.sleep(0.5)
print('-=' * 30)
print('{:^60}'.format('JOGO DA MEGA SENA'))
print('-=' * 30)

from random import randint
from time import sleep
lista = []
jogos = list()
tot = 1
quant = int(input('Quantos jogos você quer que eu sorteie?'))
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}:{l}')
    sleep(0.5)
