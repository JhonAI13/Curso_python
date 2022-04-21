#073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética.
#d) Em que posição está o time da Chapecoense.
f = ('Palmeiras', 'Bragantino', 'Atlético-MG', 'Fortaleza EC', 'Athletico-PR', 'Bahia', 'Fluminense',
     'Flamengo', 'Santos', 'Atlético',  'Ceará', 'Corinthians', 'Juventude', 'São Paulo', 'Internacional',
     'América-MG', 'Sport', 'Cuiabá', 'Chapecoense', 'Grêmio')
print('Os 5 primeiros times são:', f[0:5])
print('Os últimos 4 colocados:', f[-4:])
print('Times em ordem alfabética:', sorted(f))
print(f'''Em que posição está o time da Chapecoense:{f.index('Chapecoense')+1}º.''')
