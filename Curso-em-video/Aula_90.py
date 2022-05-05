'''Faça um programa que leia nome e média de um aluno,
 guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.'''

d = {}
d['Nome'] = str(input('Nome: '))
d['média'] = float(input((f'Média de {d["Nome"]}: ')))
print("=-" * 15)
if d['média'] > 7:
    d['situação'] = 'aprovado'
elif d['média'] > 3:
    d['situação'] = 'recuperação'
else:
    d['situação'] = 'reprovado'
for x, v in d.items():
    print(f'    -{x} é igual a {v}.')
