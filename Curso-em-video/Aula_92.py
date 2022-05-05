'''092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o
(com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá
também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos
 a pessoa vai se aposentar.'''

from datetime import date

d = {}
data = date.today().year
d['Nome'] = str(input('Nome: '))
Ano_de_nascimento = int(input('Ano de Nascimento: '))
d['Idade'] = data - Ano_de_nascimento
d['Cateira de Trabalho'] = int(input('Carteira de Trabalho (0 ñ tem): '))
if d['Cateira de Trabalho'] != 0:
    d['Ano de contratação'] = int(input('Ano de Contratação: '))
    d['Salário'] = int(input('Salário: R$'))
    d['Aposentadoria'] = (d['Ano de contratação'] - data) + 30
print('-=' * 30)
for q, w in d.items():
    print(f'{q} é {w}')

