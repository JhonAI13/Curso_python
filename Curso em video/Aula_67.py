# Faça um programa que mostre a tabuada de varios numeros, um de cada vez, para cada valor digitado pelo usuario.
# O programa sera interrompido quando o numero solicitado for negativo
c = 0
while True:
    c = 0
    t = int(input('Qual numero quer fazer a taboada:'))
    if t < 1:
        break
    while True:
        c += 1
        cont = c * t
        print(f'{t} X {c} = {cont}')
        if c == 10:
            break
print('Acabou')
