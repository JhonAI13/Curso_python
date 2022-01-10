#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math 
o = float(input('Qual o angulo?:'))
a = math.radians(o)
print('O seno é:{:.2f} \nO coseno é:{:.2f} \nO trangente é:{:.2f} '.format(math.sin(a), math.cos(a), math.tan(a)))
