# x = 10
# def soma(x):
#     x += 3


# def modificalista(a):
#     a[0] += 10 

# a = [1,2,3,4]
# modificalista(a)
# print(a)

"""Escrva uma função que recebe um inteiro m e outro n e com isto constrói uma matriz mxn"""

# matriz = []
# m = int(input("Digite o número de linhas da matriz: "))
# n =int(input("Digite o número de colunas da matriz: "))
# def constroiMatriz (m, n, matriz):
#     for i in range (1, m+1):
#         linha = []
#         for j in range (1,n+1):
#             x = int(input(f"Digite o elemento {i}{j} da matriz: "))
#             linha.append(x)
            
#         matriz.append(linha)


"""Escreva uma função que troca um elemento por outro numa matriz"""

# def TrocaElemento(pos1, pos2, matriz):
#     pos1 = (pos1 // 10)-1
#     pos2 = (pos2 % 10)-1
#     elemento1 = matriz[pos1][pos1]
#     elemento2 = matriz[pos2][pos2]
#     matriz[pos1][pos1] = elemento2
#     matriz[pos2][pos2] = elemento1

# constroiMatriz(m, n, matriz)
# print(matriz)
# pos1 = int(input("Digite a posição do elemento 1: "))
# pos2 = int(input("Digite a posição do elemento 2: "))
# TrocaElemento(pos1, pos2, matriz)
# print(matriz)

"""Escreva uma função que gera uma matriz 4x4 com os números de 0 a 15 sem repetições"""

import random
matriz = []
def geraMatriz (matriz):
    lista = list(range(16))
    while len(lista) > 0 :
        linha = []
        for i in range(4):
            x = random.choice(lista)
            linha.append(x)
            lista.remove(x)
        matriz.append(linha)

for i in range(3):
    matriz = []
    geraMatriz(matriz)
    print(matriz)