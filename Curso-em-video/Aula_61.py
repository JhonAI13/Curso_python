# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.
p = int(input('Primeiro termo:'))
r = int(input('Razão pa:'))
s = 1
while s != 10:
    if s == 1:
        print(p, end=' => ')
    p = p + r
    s += 1
    print(p, end=' => ')
print('FIM')
