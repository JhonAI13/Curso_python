#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se
# alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa
# também deverá mostrar o tempo que falta ou que passou do prazo.

import datetime
data = int(input("Diga o ano em que nasceu:"))
data = datetime.date.today().year - data
if data < 18:
    print("Voce ainda vai se alistar, faltam {} anos".format(18 - data))
elif data == 18:
    print("Esta é a hora exata de se alistar ".format(18 - data))
elif data > 18:
    print("O tempo de se alistar ja passou em {} anos".format((18 - data)-(2*(18 - data))))
