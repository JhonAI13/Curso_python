# #  077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# #  Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
# p = ('Lapis', 'Borracha', 'Caderno', 'Estojo', 'Transferidor',
#      'Compasso', 'Mochila', 'Canetas', 'Livro')
# v = ('a', 'e', 'i', 'o', 'u')
# for c in range(0, len(p)):
#     print(f'Na palavra {p[c].upper() } temos: ', end='')
#     for x in range(0, len(p[c])):
#         if p[c][x].lower() in v:
#             print(p[c][x].lower(), end=' ')
#     print(" ")

p = ('Lapis', 'Borracha', 'Caderno', 'Estojo', 'Transferidor',
     'Compasso', 'Mochila', 'Canetas', 'Livro')
for c in range(0, len(p)):
    print(f'\nNa palavra {p[c].upper() } temos: ', end='')
    for x in range(0, len(p[c])):
        if p[c][x].lower() in 'aeiou':
            print(p[c][x].lower(), end=' ')


