#079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
#Caso o número já exista lá dentro, ele não será adicionado. No final,
#serão exibidos todos os valores únicos digitados, em ordem crescente.
l = []
x = l1 = teste = 0
c = ''
while True:
    l1 = int(input('Digite o numero:'))
    if x == 0: # Quando for a primeira vez ele so adiciona o L1.
        teste += 1
        l.append(l1)
        print('Valor adicionado com sucesso...')
    else: # Quando não for a primeira vez
        for f in range(0, len(l)): # teste para saber se o numero foi repetido.
            if l[f] != l1:
                teste += 1
        if teste == len(l): # Se não for ele adiciona
            l.append(l1)
            print('Valor adicionado com sucesso...')
        else: # Se for ele não adiciona
            print('Valor duplicado! Não vou adicionar...')
    x += 1
    teste = 0
    c = str(input('Você quer continuar[S/N]?:')).strip().upper()[0]
    while c not in "SsNn":
        c = str(input("""Dados invalidos....
    Você quer continuar[S/N]?:""")).strip().upper()[0]
    if c in 'Nn':
        break
print(sorted(l))
