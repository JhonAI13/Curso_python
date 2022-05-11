"""
Tabela ASCII
"""

# for i in range(256):
#     print(f"{i:0>3} - {chr(i)}")
    
# print(ord("😎"))
# print('A' < "a")

"""
Faça duas funções: Uma que coloque uma string em maiusculo e outra que coloque uma em minusculo.
"""

# def main ():
#     string = "CHicHetE"

#     print(tudoMaiusculo(string))
#     print(tudoMinusculo(string))


# def tudoMinusculo(string):
#     minusculo = ""

#     for char in string:
#         if "A" <= char <= "Z":
#             char = chr(ord(char) + (ord('a') - ord('A')))
#         minusculo += char
#     return minusculo

# def tudoMaiusculo(string):
#     maiusculo = ""

#     for char in string:
#         if "a" <= char <= "z":
#             char = chr(ord(char) - (ord('a') - ord('A')))
#         maiusculo += char
#     return maiusculo

# main()

"""
Faça um programa que verifique se uma letra digitada é "F' ou "M". Conforme a letra escrever>: F - Feminino, M - Masculino, Sexo Invalido.
"""

# x = input("Digite uma letra: ")
# if x == "M" or x == "m":
#     print("M - masculino")
# elif x == "F" or x == 'f':
#     print("F - Feminino")
# else:
#     print("Entrada invalida.")

"""
Faça um programa que leia um nome de usuraio e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a perdir as informações.
"""
# def main():
#     nome = input("Digite o nome de usuário: ")
#     senha = input("Digite a senha: ")
#     while tudoMaiusculo(nome) == tudoMaiusculo(senha):
#         print("Não pode senha igual a nome")
#         senha = input("Digite a senha: ")


# def tudoMaiusculo(string):
#     maiusculo = ""

#     for char in string:
#         if "a" <= char <= "z":
#             char = chr(ord(char) - (ord('a') - ord('A')))
#         maiusculo += char
#     return maiusculo

# main()



print("abc" in "abcdefghijklm")