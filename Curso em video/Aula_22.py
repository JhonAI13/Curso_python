#crie um programa que leia o nome completo de uma pessoa e mostre: O nome com todas asa letras maiusculas;Com todas as letras minusculas;
#Quantas letras aotodo sem considerar espaços .;Quantastas letraas tem o primeiro nome.
nome = input('Qual seu nome todo:')
print('Seu nome em maiusculo é:', nome.upper())
print('Seu nome em minusculo é:', nome.lower())
print('Seu nome tem {} letras ao todo.'.format(len(nome) - nome.count(' ')))
n = nome.split()
print('Seu primeiro nome tem {} letras.'.format(len(n[0])))
