#  Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
ma = 0
me = 0
c = 0
for c in range(5):
    c += 1
    p = float(input('Qual peso da {}ª pessoa:'.format(c)))
    if c == 1:
        me = p
        ma = p
    else:
        if p > ma:
            ma = p
        elif p < me:
            me = p
print("""O maior peso é {}Kg
O menor peso é {}Kg""".format(ma, me))
