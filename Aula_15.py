#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais
#ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
k = float(input('Quantos km percorreu?:'))
d = int(input('Quantos dias ficou com o carro?:'))
c =  (d * 60) + (k * 0.15)
print('O valor pago sera de:',c)
