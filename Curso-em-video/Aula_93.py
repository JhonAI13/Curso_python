# '''093: Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida. No final,
# tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.'''
#
#
# d = {}
# gols = []
# total = 0
# d['nome'] = str(input('Nome do jogador: '))
# partidas = int(input(f'Quantas partidas o {d["nome"]} jogou? '))
# d['gols'] = gols
# d['total'] = 0
# for q in range(1, partidas + 1):
#     gols.append(int(input(f'Quantos gols na partida {q}: ')))
#     d['total'] = d['total'] + 1
# print('-=' * 30)
# print(d)
# print('-=' * 30)
# for w, e in d.items():
#     print(f'O campo {w} tem o valor {e}.')
# print('-=' * 30)
# print(f'O jogador {d["nome"]} jogou {len(d["gols"])} partidas.')
# for c, v in enumerate(d['gols']):
#     print(f'   => Na partida {c + 1}, fez {v} gols. ')
#     total = d['gols'][c] + total
# print(f'Foi um total de {total} gols.')

d = {}
gols = []
total = 0
d['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas o {d["nome"]} jogou? '))
d['gols'] = gols
d['total'] = 0
for q in range(1, partidas + 1):
    gols.append(int(input(f'Quantos gols na partida {q}: ')))
d['total'] = sum(gols)
print('-=' * 30)
print(d)
print('-=' * 30)
for w, e in d.items():
    print(f'O campo {w} tem o valor {e}.')
print('-=' * 30)
print(f'O jogador {d["nome"]} jogou {len(d["gols"])} partidas.')
for c, v in enumerate(d['gols']):
    print(f'   => Na partida {c + 1}, fez {v} gols. ')
print(f'Foi um total de {d["total"]} gols.')
