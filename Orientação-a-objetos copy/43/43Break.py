# for i in range (10):
#     print(i)
#     if i == 5:
#         break

# i = 0
# while i < 10:
#     if i==5:
#         break
#     print(i)
#     i += 1 

# for j in range(10):
#     for i in range (10):
#         print(j,i)
#         if i == 5:
#             break
#     if j == 5:
#         break

# def criaLista():
#     lista = []
    
#     m = int(input("Digite o tamanho da lista: "))

#     for i in range(m):
#         ele = float(input(f"Digite o elemento {i+1} de {m}: "))
#         lista.append(ele)

#     return lista


# def main():
#     l1 = criaLista()

#     n = int(input("Digite o número de elementos que se deseja somar: "))

#     soma = 0
#     for i in range(len(l1)):
#         if i == n:
#             break
#         soma += l1[i]

#     print(f"A soma é {soma}")

# main()

# for i in range(10):
#     if i == 5:
#         continue
#     print(i)

"""
Escreva um programa que pegue a lista abaixo e forneça uma nova lista apenas com números ímpares
"""

lista= [788, 587, 61, 309, 426, 420, 801, 178, 80, 329, 831, 524, 545, 475,
        815, 958, 190, 41, 901, 432, 435, 6, 137, 679, 36, 243, 604, 826,
        758, 304, 319, 507, 404, 792, 105, 667, 438, 693, 802, 165, 527,
        814, 548, 96, 683, 602, 302, 219, 376, 914, 478, 175, 360, 266,
        555, 306, 223, 547, 214, 387, 62, 919, 908, 899, 772, 363, 270,
        723, 346, 921, 424, 75, 869, 250, 969, 633, 460, 108, 808, 5, 631,
        766, 846, 303, 600, 683, 343, 258, 904, 194, 111, 245, 412, 552,
        631, 49, 170, 246, 702, 783]
limpar = []
for i in lista:
    if i % 2 == 0 :
        continue
    limpar.append(i)
print(limpar)
