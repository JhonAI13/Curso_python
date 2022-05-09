"""097: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

Ex:
escreva('Olá, Mundo!')
Saída:
~~~~~~~~~
 Olá, Mundo!
~~~~~~~~~"""


def entre_linhas(mensagem):
    l = len(mensagem) + 2
    print('-' * l)
    print(f' {mensagem}')
    print('-' * l)


entre_linhas('Gustavo Guanabara')
entre_linhas('Curso de python no youtube')

