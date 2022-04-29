# Escreva uma função que obtenha a soma de varios números de entrada

# O asterisco é quando não sei a quantidade de argumentos.
def soma(*lista):
    # Python so aceita asterisco se for no ultimo argumento
    soma_num = 0
    # print(type(lista)) retorna <class 'tuple'>

    for num in lista:
        soma_num += num
    
    return soma_num


print(soma(1,2,3,4,5))

# Exemplo: Peso de provas

def media(p1,p2,p3,peso1=1,peso2=1,peso3=1):
    # Argumentos predefinidos tambem precisam estar no final.
    return (p1*peso1 + p2*peso2 + p3*peso3)/soma(peso1,peso2,peso3)


print(media(5,3,4))

# função que obtenha o maior número de uma seguencia de números
def maior(*lista):
    return max(lista)
# função que obenha multiplicação de varios números de entrada
def multiplicação(*lista):
    mult_num = 1
    for a in lista:
        mult_num *= a
        print(a)

    return mult_num
