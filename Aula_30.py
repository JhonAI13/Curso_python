# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele
# foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
v = int(input("Digite a velocidade do seu carro:"))
if v <= 80:
    print("Tenha uma boa viagem!")
else:
    vv = v - 80
    m = vv * 7
    print("Voce ultrapassou a velocidade de 80km. ")
    print("Sua multa é de {}Reais".format(m))
 