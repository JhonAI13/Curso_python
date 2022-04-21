# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.
p = int(input('Primeiro termo:'))
r = int(input('Razão pa:'))
i = 1
s = 10
c = 1
print('{}!'.format(p), end=' = ')
print(p, end=' => ')
while i != 0:
    while s != 1:
        p += r
        print(p, end=' => ')
        s -= 1
        c += 1
    print('PAUSE')
    i = int(input('''Que continuar?
Digite 0 parar encerrar.
Se não quantas vezes quer fazer:'''))
    s = i + 1
print('''FIM 
Teve {} termos'''.format(c))
