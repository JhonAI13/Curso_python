#Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder
# 30% do salário ou então o empréstimo será negado.

print('$'*60)
print('Olá sou do banco Itanu, vim aqui te dar um emprestimo.')

s = float(input('Qual seu salario mensal:'))
c = float(input('Qual o valor da casa que quer comprar:'))
m = int(input('Em quantos anos quer pagar:'))

#tirar 30% do salario
s1 = s * 0.3
#transformar anos em meses
m1 = m * 12
#descobir o valor das parcelas
v = c / m1

if v >= s1:
    print('Seu financiamento não foi liberado')
else:
    print('Seu financiamento foi aprovado!')
    print('Você deverar pagar por mes o valor de {:.2f}reais por {:.0f}meses'.format(v, m1))
    print('$' * 60)
