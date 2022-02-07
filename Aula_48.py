"""#  Faça um programa que calcule a soma entre todos os números que
# são múltiplos de três e que se encontram no intervalo de 1 até 500.
t = 0
for c in range(3, 500, 3):
    t += c
print(' ',t)
"""
#  Faça um programa que calcule a soma entre todos os números que
# impares que são múltiplos de três e que se encontram no intervalo de 1 até 500.
s = 0
cont = 0
for c in range(1, 500, 2):
    if c // 3 == c / 3:
        cont = cont + 1
        s += c
print('A soma de todos os {} valores solicitados é {} '.format(cont,s))
