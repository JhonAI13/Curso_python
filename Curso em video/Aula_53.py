# # Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
# f = input('Digite a fraze:').upper()
# f = f.split()
# f = "".join(f)
# c = len(f)
# print(f, end=' ')
# h = 0
# i = ''
# l = 0
# for x in range(c,0,-1):
#     i = f[h]
#     h += 1
#     g = f[x - 1]
#     print(g, end='')
#     if i == g:
#         l += 1
# if l == c:
#     print("""
# É um palindromo!""")
# else:
#     print("""
# Não é um palindromo""")

"""# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
frase = str(input('Digite uma frase: ')).lower().strip().replace(' ', '')
invertida = frase[::-1]
if frase == invertida:
    print('Esta frase É um palíndromo!')
else:
    print('A frase NÃO é um palíndromo!')
"""

# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
f = input('Digite a fraze:').upper()
f = f.split()
j = "".join(f)
i = ''
for letra in range(len(j) - 1, -1, -1):
    i += j[letra]
if i == j:
    print("Temos um palindromo!")
else:
    print('Não temos um palindromo"')
