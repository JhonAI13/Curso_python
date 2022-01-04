#Crie um algoritimo que leia um numero e mostre o seu dobro triplo e a raiz quadrada
n = int(input('Qual numero?:'))
print('O o dobro de  {} é :{}'.format(n, n * 2))
print('O triplo de {} é :{}'. format(n, n * 3))
print('A raiz quadrado de {} é:{}'.format(n, int(n ** (1 / 2))))
