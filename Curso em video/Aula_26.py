#Faça um programa que leia uma frase pelo teclado e mostre: Quantas vezes aparece a letra 'a' ;em que posição ela aparece a primeira vez
#Em que posição ela aparece pela ultima vez
f = input('Digite uma fraze:').upper().strip()
print('A letra "a" aparece {} vezes.'.format(f.count('A')))
print('A letra "a" arece ne primeira ves:', f.find('A')+1)
#O r foi colocado para que a função funcione da direita para esquerda
print('A ultima letra A apareceu na posição', f.rfind('A')+1)

