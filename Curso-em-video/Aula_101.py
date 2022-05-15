# """ 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro
# o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO,
#  OPCIONAL e OBRIGATÓRIO nas eleições."""
#
# from datetime import date
#
#
# def voto(num=0):
#     data = date.today().year
#     idade = data - num
#
#     if idade < 16:
#         print(f'Com {idade}: NÃO VOTA')
#     elif 16 <= idade < 18:
#         print(f'Com {idade}: VOTO OPIONAL')
#     else:
#         print(f'Com {idade}: VOTO OBRIGATÓRIO')
#
#
# num = int(input('Em que ano você nasceu? '))
# voto(num)
#

def voto(num=0):
    from datetime import date
    data = date.today().year

    idade = data - num

    if idade < 16:
        print(f'Com {idade}: NÃO VOTA')
    elif 16 <= idade < 18 or idade > 65:
        print(f'Com {idade}: VOTO OPIONAL')
    else:
        print(f'Com {idade}: VOTO OBRIGATÓRIO')


voto(int(input('Em que ano você nasceu? ')))
