# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
# Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8
print('='*50)
q = int(input("Quantos termos coçê quer mostrar?: "))
q -= 2
print('='*50)
x = 0
fn = 0
f = 1
print('~'*50)
print('{} => {} => '.format(fn,f), end='')
while q != 0:
    q -= 1
    x = fn + f
    print(x, end=' => ')
    fn = f
    f = x
print('Acabou')
print('~'*50)
