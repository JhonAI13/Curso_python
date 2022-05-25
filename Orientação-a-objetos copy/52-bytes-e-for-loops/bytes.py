arquivo = open('teste.txt', "w")
arquivo.write("Ola\n")
arquivo.write("Meu\n")
arquivo.write("Nome\n")
arquivo.write("é\n")
arquivo.write("Jonathas\n")
arquivo.close()

arquivo = open("teste.txt", "rb")
print(arquivo.readline())
arquivo.close()

arquivo = open("teste.txt", "r")
print(arquivo.seek(8))
print(arquivo.readline())
print(arquivo.readline())
print(arquivo.tell())
print(arquivo.read(1))
print(arquivo.readline(1))
print(arquivo.readlines(1))
arquivo.close()

arquivo = open("teste.txt", "r")
# for x in arquivo:
#     print(x)
for x in arquivo.readline():
    print(x)
    print("-")
arquivo.close()
"Para fazer uma lista no txt"
# l = [1,2,3]
# l = eval(l)
