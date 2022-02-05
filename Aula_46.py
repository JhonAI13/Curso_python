"""# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
# indo de 10 até 0, com uma pausa de 1 segundo entre eles.

import time
print('Os fogos serão lançados em 10 segundos')
time.sleep(1)

t = 11
for c in range(11,0,-1):
    t += -1
    print(t)
    if t == 0:
        break
    time.sleep(1)
print('Fogo')

"""
# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
# indo de 10 até 0, com uma pausa de 1 segundo entre eles.

import time
print('Os fogos serão lançados em 10 segundos')
time.sleep(1)
for c in range(10,-1,-1):
    print(c)
    if c == 0:
        break
    time.sleep(0.3)
print('Fogo')
