# Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
# mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
i = 's'
x = me = ma = c = m =0
while i not in 'Nn':
    x = int(input('Digite um numero:'))
    i = str(input('Quer continuar?'))
    m = x + m
    c += 1
    if c == 1:
        ma = me = x
    else:
        if x > ma:
            ma = x
        if x < me:
            me = x
print('A media é dos valore é :{}'.format(m / c))
print('O maior numero é {} e o menor numero é {}'.format(ma, me))
