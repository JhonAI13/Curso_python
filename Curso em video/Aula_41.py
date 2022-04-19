#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#- Até 9 anos: MIRIM
#- Até 14 anos: INFANTIL
#- Até 19 anos: JÚNIOR
#- Até 25 anos: SÊNIOR
#- Acima de 25 anos: MASTER

import datetime
print("Este programa dira qual sua categoria na natação.")
c = int(input("Qual ano você nasceu:"))
data = datetime.date.today().year
c = (c - data) - 2 * (c - data)
if c < 9.1:
    print("MIRIM")
elif c < 14.1 and c > 9:
    print("INFANTIL")
elif c < 19.1 and c > 14:
    print("JÚNIOR")
elif c < 25.1 and c > 19:
    print("SÊNIOR")
elif c > 25:
    print("MASTER")
