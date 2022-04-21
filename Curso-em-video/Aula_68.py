# Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder, mostrando
# o total de vitórias consecutivas que ele conquistou no final do jogo.
import random
n = r = c = 0
while True:
    n = random.randrange(1,11)
    q = int(input('Digite um numero:'))
    pi = str(input('Digite [P/I]:'))
    print(f'O Computador escolheu {n}')
    r = n + q
    if r // 2 == r / 2:
        print(f'{r} é Par')
        if pi in "Ii":
            print('Voce perdeu!')
            break
        else:
            print('Voce ganhou!')
            c += 1
    else:
        print(f'{r} é Impar')
        if pi in "Pp":
            print('Voce perdeu!')
            break
        else:
            print('Voce ganhou!')
            c += 1
    print('~^'*50)
print(f'Você ganhou {c} vezes.')
