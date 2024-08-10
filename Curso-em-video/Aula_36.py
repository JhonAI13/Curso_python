print('$'*60)  # Imprime uma linha de 60 caracteres '$' para fins de formatação visual
print('Olá sou do banco Itanu, vim aqui te dar um emprestimo.')  # Mensagem de boas-vindas ao usuário

salario = float(input('Qual seu salario mensal:'))  # Solicita ao usuário o salário mensal e converte a entrada para um número de ponto flutuante
valor_casa = float(input('Qual o valor da casa que quer comprar:'))  # Solicita o valor da casa desejada e converte para um número de ponto flutuante
prazo_anos = int(input('Em quantos anos quer pagar:'))  # Solicita o prazo do financiamento em anos e converte para um número inteiro

# Cálculo do limite máximo da parcela: 30% do salário
limite_parcela = salario * 0.3  # Calcula o limite máximo da parcela como 30% do salário

# Conversão de anos para meses
prazo_meses = prazo_anos * 12  # Calcula o prazo do financiamento em meses

# Cálculo do valor da parcela mensal
valor_parcela = valor_casa / prazo_meses  # Calcula o valor da parcela mensal dividindo o valor da casa pelo número de meses

# Verificação da aprovação do financiamento
if valor_parcela >= limite_parcela:  # Verifica se o valor da parcela excede o limite máximo
    print('Seu financiamento não foi liberado')  # Imprime uma mensagem informando que o financiamento foi negado
else:
    print('Seu financiamento foi aprovado!')  # Imprime uma mensagem informando que o financiamento foi aprovado
    print('Você deverar pagar por mes o valor de {:.2f}reais por {:.0f}meses'.format(valor_parcela, prazo_meses))  # Imprime o valor da parcela e o prazo do financiamento em meses
    print('$' * 60)  # Imprime outra linha de 60 caracteres '$' para fins de formatação visual