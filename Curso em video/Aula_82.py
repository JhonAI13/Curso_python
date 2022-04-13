# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores
# pares e os valores ímpares digitados, respectivamente. Ao final,
# mostre o conteúdo das três listas geradas.
l = []
i = []
p = []
while True:
    l.append(int(input('Digite um valor:')))
    c = str(input('Você quer continuar[S/N]?:')).strip().upper()
    while c not in "SsNn":
        c = str(input("""Dados invalidos....
Você quer continuar[S/N]?:""")).strip().upper()
    if c in 'Nn':
        break
for x in range(0, len(l)):
    if l[x] / 2 == l[x] // 2:
        p.append(l[x])
    else:
        i.append(l[x])
print(f'''Alista é :{l}
Os numeros pares da lista são:{p}
Os numeros impares da lista são:{i}''')
