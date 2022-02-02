#Crie um programa que faça o computador jogar Jokenpô com você.

import random
print("""Joqueipô
[1] Pedra
[2] Papel
[3] Tesoura""")
e = int(input("Qual escolhe:"))

r = 1
p = 2
t = 3

p = (r, p, t)
u = random.choice(p)

if e == u:
    print("A maquina escolheu {}".format(u))
    print("Empatou")
elif e == 1 and u == 3 or e == 2 and u == 1 or e == 3 and u == 2:
    print("A maquina escolheu {}".format(u))
    print("Você venceu!")
elif e == 1 and u == 2 or e == 2 and u == 3 or e == 3 and u == 1 :
    print("A maquina escolheu {}".format(u))
    print("Você perdeu!")
