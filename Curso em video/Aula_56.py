#  Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
h = 0
me = 0
sm = 0
r = 4
for x in range(1, r + 1):
    print('------{}ªPessoa------'.format(x))
    n = str(input('Qual o nome: '))
    i = float(input('Qual sua idade:'))
    s = str(input('Qual sexo(M/F)'))
    me = i + me
    if s == 'M' or s == 'm':
        if x == 1:
            h = i
        else:
            if i > h:
                h = i
                nh = ('O homem mais velho é o {}, ele tem {} anos.'.format(n, h))
    else:
        if i < 20:
            sm += 1
print('A media das idades é', me/r, 'anos')
print(nh)
print('Tem {} meninas com menos de 20 anos'.format(sm))
