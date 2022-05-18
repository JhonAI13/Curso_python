"""
Arquivo para os métodos find e index

Escreva uma função que receba um string e uma sub
string e verifique se a substring faz parte da string
"""
# def find(frase, sub):
#     for i in range(len(frase) + 1 - len(sub)):
#         if frase[i:i+len(sub)] == sub:
#             return i 

#     return -1

# def index(frase, sub):
#     for i in range(len(frase) + 1 - len(sub)):
#         if frase[i:i+len(sub)] == sub:
#             return i 

#     return "ERRO"

# print(find("mississipi", "ss"))

# print("python".find("on"))
"""
Arquivo para count

Escreva a seguinte função:
1. Conte o número de ocorrências de uma substring em uma string
"""
# def count(frase, sub):
#     cont = 0

#     for i in range(len(frase) + 1 - len(sub)):
#         if frase[i:i+len(sub)] == sub:
#             cont += 1

#     return cont

# print(count("mississipi", "ss"))
# print("mississipi".count("ss"))

"""
Arquivo para replace

Escreva uma função que recebe uma string, uma substring velha, e uma substring
nova e devolve uma copia da string com todas as substrings velha substituidas
pela subtring nova
"""
def replace(frase, velha,nova):
    palavra = ''
    i = 0

    while i < len(frase) + 1 - len(velha):
        if frase[i:i+len(velha)] != velha:
            palavra += frase[i]
        else:
            i += len(velha)
            palavra += nova
            continue
        i += 1

    palavra += frase[i:]
    return palavra

print(replace('mississipi', 'ss', 'zzz'))
