#Faça um proggrama que leia um numero de 0 a 9999 e mostre cada um dos digitos separados.
'''n = input('Digite um numero de 0 a 9999:')
print('unidade:',n[3])
print('desena:',n[2])
print('centena:',n[1])
print('milhar:',n[0])'''

n = int(input('Digite um numero:'))
print('unidade:', n // 1 % 10)
print('desena:', n // 10 % 10)
print('centena:', n // 100 % 10)
print('milhar:', n // 1000 % 10)

