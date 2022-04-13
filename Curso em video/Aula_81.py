# # Crie um programa que leia numeros e os coloque em uma lista. Depois mostre isto:
# # Quantos numeros foram digitados
# # A lista dos valores em ordem decrescente.
# # Se existe o numero 5
# l = []
# c = 0
# x = ' não '
# while True:
#     c += 1
#     l.append(int(input("digite um numero:")))
#     h = str(input("Você quer continuar(S/N):"))
#     if l[c - 1] == 5:
#         x = ' '
#     if h in "Nn":
#         break
# print()
# k = sorted(l)
# print(f'''Foram digitados {c} numeros!
# A lista dos valores em ordem  crescente é:{k[::-1]}
# O numero 5{x}existe na lista.''')

l = []
while True:
    l.append(int(input('Digite um valor:')))
    r = str(input('Quer continuar(S/N):'))
    if r in "Nn":
        break
print()
print(f'Você digitou {len(l)} de elemento')
l.sort(reverse=True)
print(f'Os valores em ordem decrescente são:{l}')
if 5 in l:
    print('O valor 5 faz parte da lista.')
else:
    print('O valor 5 não faz parte da lista.')
