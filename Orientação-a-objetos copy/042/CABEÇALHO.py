import numbers
import random
from tkinter import N

def VerificaEntrada(num):
    """
    Retorna um booleano dizendo se a entrada é válida
    ou não, tendo em vista o número de dígitos
    True --> Entrada Válida(4 digitos)
    False --> Entrada Inválida(-/+4 digitos)
    """
    if num > 999 and num < 10000:
        return True
    else:
        return False 


def GeraSecretNum():
    """
    Função que gera e retorna o número secreto
    E a lista contendo cada um de seus dígitos
    Exemplo
    secretNum = 1783
    list_num = [1,7,8,3]
    OBS: O NUMERO NAO PODE TER DIGITOS REPETIDOS
    """
    list_num = []
    secretNum = 0
    while True:
        r = random.randrange(0,9)
        if r in list_num or r == 0 and len(list_num) == 0:
            continue
        elif len(list_num) == 4:
            break                   
        else:
            list_num.append(r)
            if len(list_num) == 1:
                secretNum += list_num[0]
            elif len(list_num) == 2:
                secretNum += list_num[1] /10
            elif len(list_num) == 3:
                secretNum += list_num[2] /100
            else:
                secretNum += list_num[3] /1000 
                secretNum *= 1000
            
        
    return round(secretNum), list_num 


def GeraDicas(num, secretNum, secretNumList):
    """
    Recebe o número escolhido e o número secreto
    e gera uma lista contendo as dicas a serem
    colocadas.
    Código
    --> 0 = Bagels(nenhum digito certo)
    --> 1 = Pico(Esta correto mas na posição errada)
    --> 2 = Fermi(Esta correto na posição correta)

    Retorna uma lista vazia caso os dois números sejam iguais
    """
    lista = []
    # if num != secretNum:
    #     lista.append(0)
    num = number_list(num)
    for i in range(0,4):
        if num[i] == secretNumList[i]:
            lista.append(2)
            print(num[i], secretNumList[i])
    for j in range(0,4):
        if num[j] in secretNumList:
            lista.append(1)
    if lista == [2,2,2,2]:
        return lista
           

    return lista

def number_list(num):
    lista = []
    l = []
    n = round(num % 10)
    lista.append(n)
    num = round((num -(num % 10))/10)
    n = num % 10
    lista.append(n)
    num = round((num -(num % 10))/10)
    n = num % 10
    lista.append(n)
    num = round((num -(num % 10))/10)
    n = num % 10
    lista.append(n)

    for i in range(3,-1,-1):
        l.append(lista[i])
    return l


print(GeraDicas(1233,1234,[1,2,3,4]))