#Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#- à vista dinheiro/cheque: 10% de desconto
#- à vista no cartão: 5% de desconto
#- em até 2x no cartão: preço formal
#- 3x ou mais no cartão: 20% de juros

c = float(input('Quanto foi suas compras:'))
print('[ 1 ] dinheiro ou cheque')
print('[ 2 ] a vista no cartão')
print('[ 3 ] em 3x no cartão')
print('[ 4 ] 3x ou mais no cartão')
p = int(input('Qual formato de pagamento:'))
if p == 1:
	print('Você pagara{}'.format(c * 0.9))
elif p == 2:
	print('Você pagara{}'.format(c * 0.95))
elif p == 3:
	print('Você pagara 2x de {}'.format(c / 2))
elif p == 4:
	x = int(input('Em quantas vezes você pagara?:'))
	print('Você pagara {} em {} vezes '.format((c * 1.2) / x, x ))

