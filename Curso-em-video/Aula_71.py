# # 071: Crie um programa que simule o funcionamento de um caixa eletrônico.
# # No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# # e o programa vai informar quantas cédulas de cada valor serão entregues.
# # OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
# c50 = c20 = c10 = c5 = c1 = 0
# v = int(input('Qual Valor sera sacado? '))
# while True:
#     if v >= 50:
#         v -= 50
#         c50 += 1
#     elif v >= 20:
#         v -= 20
#         c20 += 1
#     elif v >= 10:
#         v -= 10
#         c10 += 1
#     elif v >= 1:
#         v -= 1
#         c1 += 1
#     if v <= 0:
#         break
# print(f'''=============================
#          BANCO CEV
# =============================
# Total de {c50} cédulas de R$50
# Total de {c20} cédulas de R$20
# Total de {c10} cédulas de R$10
# Total de {c1} cédulas de R$1''')

print('='*30)
print('{:^30}'.format('BANCO CEV'))
print('='*30)
valor = int(input('Que valor você quer sacar? R$:'))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -=ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R$:{ced}')
        if ced == 50:
            ced = 20
        elif ced ==20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('='*30)
print('Volte sempre ao BANCO CEV! Tenha um Bom dia!')
