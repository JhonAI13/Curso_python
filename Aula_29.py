#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
#descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

import  random
print("-=-"*17)
print("O jogo é, adivinhe o valor aleatorio(entre 1 a 5)")
print("-=-"*17)
n = random.randrange(5)
v = int(input("Digite o seu chute:"))
if n == v:
    print("parabens você acertou!")
else:
    print("A maquina venceu, o numero é {}".format(n))
