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

# def lista():
#     start = 0
#     lista = []
#     def incrementa(item):
#         nonlocal lista,start
#         lista.append(item)
#         start += 1
#         print(item,start)
#     return incrementa


# compras1 = lista ()
# compras1('presunto')
# compras1('mortadela')
# compras1('queijo')
# compras1('pão') 

"""
Escreva um programa usando uma nested function que permita imprimir a taboada
de 1 até um n dado

Exemplo:
>>>
Digite um número: 3
Para o número 1
1 * 1 = 1
1 * 2 = 2
1 * 3 = 3
1 * 4 = 4
1 * 5 = 5
1 * 6 = 6
1 * 7 = 7
1 * 8 = 8
1 * 9 = 9
1 * 10 = 10

Para o número 2
2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
2 * 4 = 8
2 * 5 = 10
2 * 6 = 12
2 * 7 = 14
2 * 8 = 16
2 * 9 = 18
2 * 10 = 20

Para o número 3
3 * 1 = 3
3 * 2 = 6
3 * 3 = 9
3 * 4 = 12
3 * 5 = 15
3 * 6 = 18
3 * 7 = 21
3 * 8 = 24
3 * 9 = 27
3 * 10 = 30

>>>
"""
# t = int(input('Qual numero:'))
# for c in range(1,11):
#     print(t, 'X', c, '=', c * t)

c = 0
# t = 0 
# p = ''
# def pertuntaTabuada():
#     p = int(input("Digite um número: "))
#     def tabuada(t):
#         for c in range(1,11):
#             print(t, 'X', c, '=', c * t)
#     for t in range(1,p+1):
#         print(f"Para o número {t}")
#         tabuada(t)
#         print()

# pertuntaTabuada()

# def tab(N):
#     """
#     Recebe um número N e devolve uma função mult
#     """
#     def mult(x):
#         """
#         Recebe x e devolve x*n
#         """
#         return x*N

#     return mult

# def main():
#     """
#     Função principal do programa
#     """

#     n = int(input("Digite um número: "))
    
#     for i in range(1, n+1):
#         f = tab(i)
#         print("Para o número", i)
#         for j in range(1, 11):
#             print(f'{i} * {j} = {f(j)}')
#         print()

# main()

"""
Reescreva o programa bancário da aula 36 colocando todas as funções dentro da
função main. Utilize o statement nonlocal.
(OBS: Pense bem onde colocar as variáveis "globais")
"""
def main():
    """
    Função principal do programa. Possui duas nested functions:
    criaConta e VerSaldo
    """
    contas = []
    depositos = []
    saldo = 0
    
    def criaConta():
        """
        Cria uma nova conta
        """
        nonlocal contas, depositos, saldo
        num_conta = int(input("Digite um número de conta: "))

        while num_conta in contas:
            print("Conta já existente. Digite novamente.")
            num_conta = int(input("Digite um número de conta: "))

        contas.append(num_conta)

        deposito = float(input("Digite o valor do seu primeiro depósito: "))
        while deposito <= 0:
            print("Valor de depósito inválido.")
            deposito = float(input("Digite o valor do seu primeiro depósito: "))

        depositos.append(deposito)
        saldo += deposito

    def VerSaldo():
        """
        Permite que o usuário visualize seu saldo
        """
        #nonlocal saldo --> Note que não é preciso colocar nonlocal
        #já que não modificamos o valor de saldo
        opção = bool(int(input("Deseja ver o saldo do banco(1 - Sim/ 0 - Não): ")))
        if opção:
            print("O saldo do banco é R$", saldo)



    opção = bool(int(input("Deseja ver o criar conta(1) ou fechar o programa(0): ")))
    while opção:
        criaConta()
        VerSaldo()
        opção = bool(int(input("Deseja ver o criar conta(1) ou fechar o programa(0): ")))

main()