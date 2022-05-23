""" 105: Faça um programa que tenha uma função notas() que pode receber várias notas de
alunos e vai retornar um dicionário com as seguintes informações:
- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)
Adicione também as docstrings dessa função para consulta pelo desenvolvedor."""


def notas(*n, sit=False):
    """
    Função que analiza as notas
    :param n: todas as notas
    :param sit: Se quer a situação ou não (True/False)
    :return: dicionario d
    """
    d = {}
    d['total'] = len(n)
    d['maior'] = max(n)
    d['menor'] = min(n)
    d['média'] = sum(n) / d['total']
    if sit:
        if d['média'] > 7:
            d['situação'] = 'aprovado'
        elif d['média'] > 3:
            d['situação'] = 'recuperação'
        else:
            d['situação'] = 'reprovado'
    return d


resp = notas(5, 2, 9, sit=True)
print(resp)
help(notas)
