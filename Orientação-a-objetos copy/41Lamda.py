p = (lambda mensagem : print(mensagem))


def soma(x,y,z):
    return x + y + z


f = (lambda x,y,z: x+y+z)# Bom para funções de callback

p(f(1,2,3))
p(help(f))