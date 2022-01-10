#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira. Ex: Digite
#um número: 6.127 O número 6.127 tem a parte Inteira 6.
'''num = float(input('digite um numero real?:'))
n = int(num)
print('O numero {} tem a parte inteira {}'.format(num, n))'''
'''from math  import floor
num = float(input('digite um numero real?:'))
print('O numero {} tem a parte inteira {}'.format(num, floor(num)))'''
from math  import trunc
num = float(input('digite um numero real?:'))
print('O numero {} tem a parte inteira {}'.format(num, trunc(num)))

