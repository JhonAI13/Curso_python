#  Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários
#  superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
s = int(input("Digite seu salario:"))
if s <= 1250:
    s2 = (s * 0.15) + s 
    print("Você receberar um aumento de R$:{} o para R${}0".format(s,s2))
else:
    s2 = (s * 0.10) + s
    print("Você receberar um aumento de R$:{} o para R${}0".format(s, s2))
