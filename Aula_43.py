#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#- IMC abaixo de 18,5: Abaixo do Peso
#- Entre 18,5 e 25: Peso Ideal
#- 25 até 30: Sobrepeso
#- 30 até 40: Obesidade
#- Acima de 40: Obesidade Mórbida

p = float(input('Qual seu peso?'))
a = float(input('Qual sua altura?'))

m = p / (a ** 2)

if m < 18.5:
	print('Abaixo do peso')
elif m >= 18.5 and m < 25:
	print('Peso ideal')
elif m >= 25 and m < 30:
	print('Sonbrepeso')
elif m >= 30 and m < 40:
	print('Obesidade')
elif m >= 40:
	print('Obesidade Mórbida')

