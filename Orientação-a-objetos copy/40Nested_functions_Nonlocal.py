# def f1():
#     x = 8001# Se não definir da nameerror
#     def f2():
#         print(x)
#     f2()# Se escrecer antes de declarar da local erro

# x = 10 
# def f1():
#     def f2():
#         global x 
#         x += 1
#         print(x)
#     f2()

# f1()
# # >>>11
# f1()
# # >>>12
# f1()
# # >>>14

# def exp(n):
#     def eleva(x):
#         print(x**n)
#     return eleva


# f = exp(5)
# f(2)

# def f1():
#     começo = 0
#     def f2():
#         nonlocal começo
#         print(começo)
#         começo += 1
#     return f2


# g = f1()
# g()
# # >>>0
# g()
# # >>>1
# g()
# # >>>2

def lista():
    start = 0
    lista = []
    def incrementa(item):
        nonlocal lista,start
        lista.append(item)
        start += 1
        print(item,start)
    return incrementa


compras1 = lista ()
compras1('presunto')
compras1('mortadela')
compras1('queijo')
compras1('pão') 

"Fazer exervcicios."