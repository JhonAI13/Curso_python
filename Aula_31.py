# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por
# Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
v = int(input("Digite a distancia de sua viagem:"))
if  v <= 200:
    v1 = v * 0.5
    print("O valor da sua passagem é de R${}0".format(v1))
else:
    v2 = v * 0.45
    print("O valor da sua passagem é de R${}0".format(v2))
