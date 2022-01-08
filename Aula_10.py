#Crie um programa que leia  quanto dinheiro uma pessoa tem na carteira e mostre quantos dolates ela pode comprar.
n = int(input('Quantos reais tem na carteira:'))
D = float(input('Qual a cotação atual do dolar:'))
print('Você pode comprar $:{} dolares'.format(n / D))

