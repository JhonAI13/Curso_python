# 1. Solicita ao usuário o valor do produto.
n = float(input('Qual o valor do produto?: '))

# 2. Calcula o desconto de 5% sobre o valor do produto.
desconto = n * 0.05

# 3. Calcula o novo preço do produto.
novo_preco = n - desconto

# 4. Imprime o novo preço com desconto.
print('O valor do produto descontado 5% é:', novo_preco, 'Reais')