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
        matriz = geraMatrizAleatoria(matriz)
        print(matriz)
        jogada = verificaJogada(matriz)
        trocaElementos(matriz, jogada)
        print(matriz)
        if verificaSeVenceu(matriz):
            False
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


def verificaSeVenceu(matriz):
    verificação = [[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]]
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

        if n // 10 >= 1 and n // 10 <= 4 : # Verifica se a dezena esta entre 1 a 4
            if n % 10 >= 1 and n % 10 <= 4: # Verifica se a unidade esta entre 1 a 4
                if matriz[(n//10)-1][(n%10)-1] != 0: # Verifica se o não esta no valor 0
                    print(n)
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

main()