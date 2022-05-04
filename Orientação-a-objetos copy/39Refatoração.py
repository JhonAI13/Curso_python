def fatorial(n):
    if n == 1:
        return n
    return fatorial(n-1) * n

print(fatorial(10))
"""
Escreva uma função recursiva que imprima de um numero x até um y
"""
def imprimir_de_x_a_n(x,n):
    print(x)
    if x == n:
        return x
    return imprimir_de_x_a_n(x+1,n)


imprimir_de_x_a_n(1,10)
"""
Escreva uma função recursiva que retorna a soma de n até zero
"""
def soma_n_0(n):
    a = n
    if n == 0:
        return n
    return soma_n_0(n-1) + a

print(soma_n_0(995))
