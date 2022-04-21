#O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random
z = input('Nome do aluno?:')
x = input('Nome do aluno?:')
c = input('Nome do aluno?:')
v = input('Nome do aluno?:')
u  = random.sample([z, x, c, v], k=4)
print('\nO nome escolhido foi:',u)
