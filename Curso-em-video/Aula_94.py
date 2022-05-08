# '''094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média'''
#
# d = {}
# s = []
# n = []
# i = []
# c = ''
# while True:
#     n.append(str(input('Nome: ')))
#     c = str(input('Sexo [M/F]: '))
#     while c not in "MmFf":
#         c = str(input("""Erro Responda M ou F
# Sexo [M/F]: """)).strip().upper()
#     s.append(c)
#     i.append(float(input('Idade: ')))
#
#     c = str(input('Você quer continuar[S/N]:')).strip().upper()
#     while c not in "SsNn":
#         c = str(input("""ERRO! Responda apenas S ou N.
# Você quer continuar[S/N]:""")).strip().upper()
#     if c in 'Nn':
#         break
#     print('=' * 30)
# print('-=' * 30)
# d['nome'] = n[:]
# d['sexo'] = s[:]
# d['idade'] = i[:]
# # d = {'nome': ['Joana', 'João', 'Maria', 'Ana', 'Jhon'], 'sexo': ['f', 'm', 'f', 'f', 'm'], 'idade': [56.0, 48.0, 45.0, 98.0, 32.0]}
# media = sum(d["idade"])/len(d["idade"])
# print(f'''Ao todo temos {len(d["nome"])} pessoas cadastradas.
# A média de idade é de {media:.2f}''')
# p = list()
# s = list()
# for q in range(0, len(d['nome'])):
#     if d['sexo'][q] in 'fF':
#         s.append(d['nome'][q])
#     if d["idade"][q] > media:
#         p.append(f'nome = {d["nome"][q]:<10}; sexo = {d["sexo"][q]}; idade = {d["idade"][q]:.0f}')
# print(f'''As mulheres cadastradas foram: {s}
# Lista das pessoas que estão acima da média:''')
# for e in range(0, len(p)):
#     print('      ', p[e])

pessoas=[]
media=0
cont=0
while True:
    pessoas.append({"nome":input("Nome:").title().strip()})
    pessoas[cont]["sexo"] = input("Sexo [F/M]:").upper().strip()
    while pessoas[cont]["sexo"] not in "FM":
        print("ERRO! Por favor, digite apenas M ou F.")
        pessoas[cont]["sexo"] = input("Sexo [F/M]:").upper().strip()
    pessoas[cont]["idade"] = int(input("Idade:"))
    media += pessoas[cont]["idade"]
    cont += 1
    es = input("Quer continuar?[S/N]:").strip()
    while es not in "snSN":
        print("ERRO! Responda apenas S ou N.")
        es = input("Quer continuar?[S/N]:").strip()
    if es == "n":
        break
media /= len(pessoas)
print("=-"*35)
print(f"A) Foram cadastradas {len(pessoas)} pessoas.")
print(f"B) A média de idade é de {media} anos..")
print("C) As mulheres cadstrads foram:" , end=" ")
for c in pessoas:
    if c["sexo"] == "F":
        print(c["nome"], end=" ")
print()
print("D) Lista de pessoas com a idade acima da média:")
for c in pessoas:
    if c["idade"]>media:
        for k, v in c.items():
            print(f"{k:>8} = {v:<14}", end="")
        print()
print("<< ENCERRADO >>")
