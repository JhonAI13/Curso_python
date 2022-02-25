# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram
# a maioridade e quantas já são maiores.
import datetime
p = 0
a = 0
m = 0
for x in range(6):
    p += 1
    idade = int(input('Qual a idade que a {} pessoa nasceu:'.format(p)))
    data = datetime.date.today().year - idade
    print(data)
    if data >= 18:
        a += 1
    elif data < 18:
        m += 1
print('{} Pessoas atigingiram a maior idade'.format(a))
print('{} Pessoa ainda não'.format(m))
