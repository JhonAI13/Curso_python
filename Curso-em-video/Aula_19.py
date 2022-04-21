#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,
# lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
import random
z = input('Nome do aluno?:')
x = input('Nome do aluno?:')
c = input('Nome do aluno?:')
v = input('Nome do aluno?:')
p = (z, x, c, v)
u  = random.choice(p)
print('\nO nome escolhido foi:',u)
