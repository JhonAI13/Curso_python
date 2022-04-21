#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com a apalavra 'santo'
cida = input('Digite uma cidade:')
cidade = cida.split()
if cidade[0].lower().find('sant') == 0:
    print('Esta cidade tem "santo"')
else:
    print('Esta cidade não tem "santo" no começo')
