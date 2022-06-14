import moeda2

p = float(input('Digite o preço: R$'))
print(f"""A metade de R${p} é R${moeda2.metade(p)}.
O dobro de R${p} é R${moeda2.dobro(p)}.
Aumentando 10%, temos R${moeda2.aumentar(p, 10)}""")
