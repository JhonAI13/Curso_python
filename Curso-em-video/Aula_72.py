# #072: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# # Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
# n = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'oze', 'treze', 'quatorze', 'quinze', 'dezesseis','dezessete', 'dezoito', 'dezenove', 'vinte')
#
# c = int(input('Qual numeor voce quer que eu escreva por estenço:'))
#
# while True:
#     if c >= 0 and c <= 20:
#         break
#     else:
#         c = int(input('Qual numeor voce quer que eu escreva por estenço:'))
#
# print(f'Seu numero por extenço é:{n[c]}')

n = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis','dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    c = int(input('Qual numeor voce quer que eu escreva por estenço:'))

    while True:
        if c >= 0 and c <= 20:
            break
        else:
            c = int(input('Qual numeor voce quer que eu escreva por estenço:'))
    print(f'Seu numero por extenço é:{n[c]}')
    n1 = str(input('Você quer continuar[S/N]'))
    if n1 in 'Nn':
        break
