#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
n = input('Qual seu nome todo:').strip()
e = n.split()
print('Seu primeiro nome é:', e[0])
f = n.rfind(' ') + 1
print('Seu ultimo nome é:', n[f:])
 
