""" 103: Faça um programa que tenha uma função chamada ficha(), que receba dois
 parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser
  capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente."""


def ficha(nome='<DESCONHECIDO>', gols=0):
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    if nome.strip() == '':
        nome = '<DESCONHECIDO>'
    print(f"O jogador {nome} fez {gols} gol(s) no campeonato.")


a = str(input('Nome do jogador: '))
b = str(input('Número de Gols:'))
ficha(a, b)

