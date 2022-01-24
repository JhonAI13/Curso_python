#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#- Média abaixo de 5.0: REPROVADO
#- Média entre 5.0 e 6.9: RECUPERAÇÃO
#- Média 7.0 ou superior: APROVADO

n1 = float(input("Digire a primeira nota:"))
n2 = float(input("Digite a segunda nota:"))

media = (n1 + n2) / 2

if media > 7:
    print('\033[32m'+'Sua media é {} você Foi aprovado'.format(media) +'\033[0;0m'.format(media))
    print('\033[32m'+'PARABENS!!'+'\033[0;0m')
elif media >= 5.1 and media <= 6.6:
    print('\033[33m'+'Sua media é {} você esta de recuperação.'.format(media) +'\033[0;0m'.format(media))
elif media <= 5:
    print('\033[31m'+'Sua media é {} você Foi reprovado.'.format(media) +'\033[0;0m'.format(media))
