# #  076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# #  No final, mostre uma listagem de preços, organizando os dados em forma tabular.
# p = ('Lapis', 1.75, 'Borracha', 2.00, 'Caderno', 15.00, 'Estojo', 25.00, 'Transferidor', 4.20,
#      'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
# print('-' * 39)
# print("{:^39}".format('LISTAGEM DE PREÇOS'))
# print('-' * 39)
# for c in range(18):
#     if c/2 == c//2:
#         print(p[c], end='')
#         x = len(p[c])
#         x = 30 - x
#         print('.' * x, end='')
#     else:
#         print('R$', end='')
#         print('{:>7}'.format('{:.2f}'.format(p[c])))
# print('-' * 39)

p = ('Lapis', 1.75, 'Borracha', 2.00, 'Caderno', 15.00, 'Estojo', 25.00, 'Transferidor', 4.20,
     'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('-' * 39)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 39)
for c in range(0, len(p)):
    if c/2 == c//2:
        print(f"{p[c]:.<30}", end='')
    else:
        print(f'R${p[c]:>7.2f}')
print('-' * 39)
