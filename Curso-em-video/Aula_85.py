# # 085: Crie um programa onde o usuário possa digitar sete valores numéricos
# # e cadastre-os em uma lista única que mantenha separados os valores pares e
# # ímpares. No fina mostre os valores pares e ímpares em ordem crescente.
# l = [[], [], []]
# for x in range(0, 7):
#     l[2].append(int(input('Digite um valor:')))
#     if l[2][x] / 2 == l[2][x] // 2:
#         l[1].append(l[2][x])
#     else:
#         l[0].append(l[2][x])
# print('=-'*30)
# print(f'''Os numeros pares da lista são:{sorted(l[1])}
# Os numeros impares da lista são:{sorted(l[0])}''')

l = [[], []]
for x in range(0, 7):
    v = int(input('Digite um valor:'))
    if v % 2 == 0:
        l[0].append(v)
    else:
        l[1].append(v)
print('=-'*30)
print(f'''Os numeros pares da lista são:{sorted(l[0])}                         
Os numeros impares da lista são:{sorted(l[1])}''')

