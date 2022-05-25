# arquivo = open("txt.txt", 'w')
# # "w" -> write -> escrever
# # "r" -> read -> ler
# # "a" -> append -> extender

# arquivo.write("chiclete coim banana \n")
# arquivo.write("Manga com leite")
# arquivo.writelines(['ola', 'arquivo', 'essa', 'é', 'primeira', 'aula'])
# arquivo.close()

# arquivo = open("txt.txt", 'r')
# print(arquivo.read())
# print(arquivo.readline())
# print(arquivo.readlines()) #Faz uma lista do txt
# arquivo.close()

arquivo = open("txt.txt", 'a')
arquivo.write("\nNova linha.")
arquivo.close()