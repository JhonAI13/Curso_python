#Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.
n = int(input("Digite o primeiro numero:"))
nn = int(input('Digite o segundo numero:'))
x = 0
while x != 5:
    print('''[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa''')
    x = int(input('oque voce quer que aconteça?'))
    if x == 1:
        print('{} + {} = {}'.format(n, nn, n + nn))
    elif x == 2:
        print('{} x {} = {}'.format(n, nn, n * nn))
    elif x == 3:
        if n > nn:
            print('Entre {} e {} o maior numero :{}'.format(n, nn, n))
        else:
            print('Entre {} e {} o maior numero :{}'.format(n, nn, nn))
    elif x == 4:
        n = int(input("Digite o primeiro numero:"))
        nn = int(input('Digite o segundo numero:'))
    else:
        print("Opção invalida tente novamente")
    print('-=' * 50)
print('Acabou!')
