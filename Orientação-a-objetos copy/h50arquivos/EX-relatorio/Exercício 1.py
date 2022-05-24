"""
A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em
disco no seu servidor de arquivos. Para tentar resolver este problema, o
Administrador de Rede precisa saber qual o espaço ocupado pelos usuários, e
identificar os usuários com maior espaço ocupado. Através de um programa,
baixado da Internet, ele conseguiu gerar o seguinte arquivo, chamado
"usuarios.txt":

alexandre       456123789
anderson        1245698456
antonio         123456456
carlos          91257581
cesar           987458
rosemary        789456125

Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo,
você deve criar um programa que gere um relatório, chamado "relatório.txt", no
seguinte formato:

ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso

1    alexandre       434,99 MB             16,85%
2    anderson       1187,99 MB             46,02%
3    antonio         117,73 MB              4,56%
4    carlos           87,03 MB              3,37%
5    cesar             0,94 MB              0,04%
6    rosemary        752,88 MB             29,16%

Espaço total ocupado: 2581,57 MB
Espaço médio ocupado: 430,26 MB

O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em
memória, caso sejam necessários, de forma a agilizar a execução do programa.
A conversão da espaço ocupado em disco, de bytes para megabytes deverá ser feita
através de uma função separada, que será chamada pelo programa principal.
O cálculo do percentual de uso também deverá ser feito através de uma função,
que será chamada pelo programa principal.
"""

def main():
    ""
    
    arquivo = abrir_arquivo("usuarios.txt")
    # arquivo2 = open("relatório.txt", "w")
    tol = conversor(total(arquivo))
    p = """ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso\n"""
    c = 0
    for i in range(0,12,2):
        c += 1
        p += f"{c}    "
        espaços = (14-len(arquivo[i]))*" "
        p += f"{arquivo[i]}{espaços}"
        stri = arquivo[i+1]
        con = conversor(int(stri))
        espaços = (11-len(f"{con:.2f} MB"))*" "
        p += f"{espaços}{con:.2f} MB"
        media = f"{((con)/tol)*100:.2f}%"
        espaços = (18-len(media))*" "
        p += f'{espaços}{media}\n'

    p += f'\nEspaço total ocupado: {tol:.2f} MB \nEspaço médio ocupado: {tol/6:.2f} MB'
    abrirArquivoEColocar(p)
def conversor (b):
    "bytes para megabytes"
    megabytes = b / 1048576
    return megabytes
def percentual(unitario, total):
    "% do total pelas pessoas"
    per = (unitario / total) *100
    return per
def abrir_arquivo(aqu):
    """Abrir o arquivo.
    Retona o escrito no arquivo em uma str"""
    arquivo = open(f"{aqu}", "r")
    s = arquivo.read().split()
    arquivo.close()
    return s
def total(lista):
    "Somar para obter o total"
    total = 0
    for i in range(1,13,2):
        total += int(lista[i])
    return total 
def abrirArquivoEColocar(escreva):
    arquivo = open(f"relatório.txt", "w")
    arquivo.write(f"{escreva}")
    arquivo.close()

main()