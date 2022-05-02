"""
Escreva o jogo dos números como descrito na aula. Utilize as funções escritas
em aula e mais três feitas agora:
    1 - VerificaSeVenceu: Recebe uma matriz 4x4 e verifica se os números estão
    ordenados de forma que o jogador venceu
    2 - VerificaJogada: Verifica se a jogada escolhida pelo usuário é válida
    3 - ImprimeJogo: Função que imprime o jogo na tela do usuário
Você pode fazer quantas funções adcionais quanto quiser

Organize o seu jogo dentro da função main. Dê para o usuário a toda rodada
a opção de desistir(0) ou de inserir uma posição(1), a posição inserida
será feita colocando a linha e coluna da matriz, por exemplo 11 significa que
estamos nos referenciando ao elemento da linha 1 coluna 1, 32 se referencia ao
elemento da linha 3 coluna 2
"""
import random


matriz = []


def main ():
    while True:
        geraMatrizAleatoria(matriz)
        while True:
            jogada = verificaJogada(matriz)
            trocaElementos(matriz, jogada)
            imprimeJogo(matriz)
            if verificaSeVenceu(matriz):
                break
        print("Você venceu, parabêns!!!!!")
        v = input("Quer começar novamente(0) \nPara acabar(1):")
        if v != 1:
            break
            
    print("Acabou!!")


def geraMatrizAleatoria (matriz):
    lista = list(range(16))
    while len(lista) > 0 :
        linha = []
        for i in range(4):
            x = random.choice(lista)
            linha.append(x)
            lista.remove(x)
        matriz.append(linha)
    return matriz


def verificaSeVenceu(matriz):
    verificação = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]
    if matriz[:] == verificação[:]:
        return True
    return False


def verificaJogada(matriz):
    while True:
        print("Ex: coluna 2 linha 1= 21")

        try:
            n = int(input("Em qual loca: "))
        except:
            continue 
            print("Esta errado!!!")

        linha = (n//10)-1
        coluna = (n%10)-1
        linha_zero = ondezero(matriz, n-1)//10
        coluna_zero = ondezero(matriz, n-1)%10

        if matriz[(n//10)-1][(n%10)-1] != 0: # Verifica se o não esta no valor 0
            if (linha == linha_zero -1 and coluna == coluna_zero) or (linha == linha_zero and (coluna == coluna_zero-1 or coluna == coluna_zero+1)) or (linha == linha_zero+1 and coluna == coluna_zero):
                return n


def ondezero(matriz, jogada):
    for i in range(4):
        for j in range(4):
            if matriz[i][j] == 0:
                n = ((i)*10)+(j)
                return n


def trocaElementos(matriz,jogada):
    zero1 = ondezero(matriz, jogada)//10 
    zero2 = ondezero(matriz, jogada)%10 
    jog1 = (jogada // 10) - 1
    jog2 = (jogada % 10) - 1
    elemento1 = matriz[zero1][zero2]
    elemento2 = matriz[jog1][jog2]
    matriz[zero1][zero2] = elemento2
    matriz[jog1][jog2] =  elemento1


def imprimeJogo(matriz):
    for i in range(4):
        print()
        for j in range(4):
            if matriz[i][j] >= 10:
                print(matriz[i][j], end=' ')
            elif matriz[i][j] == 0:
                print('  ', end=' ')
            else: 
                print(matriz[i][j], end='  ')
    print()


main()