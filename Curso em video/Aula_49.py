"""#  mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
t = int(input('Qual numero:'))
for c in range(1,11):
    cont = c * t
    print(t, 'X', c, '=', cont)
"""
#  mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
t = int(input('Qual numero:'))
for c in range(1,11):
    print(t, 'X', c, '=', c * t)
