#  Crie um programa que leia a idade e o sexo de várias pessoas.
#  A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.
s = ''
n = c18 = ch = cm20 = c = 0
print('~^'*50)
while True:
    s = str(input("Qual seu Sexo[F/M]:")).strip().upper()[0]
    while s not in "MmFf":
        s = str(input("""Dados invalidos.
Qual seu Sexo[F/M]:""")).strip().upper()[0]
    n = int(input('Qual sua idade:'))
    #Calculos estatisticos
    if n > 18:
        c18 += 1
    if s in 'Mm':
        ch += 1
    if s in 'Ff' and n < 20:
        cm20 += 1
    c = str(input('Você quer continuar[S/N]?:')).strip().upper()[0]
    while c not in "SsNn":
        c = str(input("""Dados invalidos.
Você quer continuar[S/N]?:""")).strip().upper()[0]
    print('~^' * 50)
    if c in 'Nn':
        break
print(f'''Tem {c18} Pessoas que tem mais de 18 anos.
Tem {ch} homens nesta lista.
Tem {cm20} Mulheres com menos de 20 anos.  ''')
print('~^'*50)
