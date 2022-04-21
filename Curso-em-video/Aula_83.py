# # Crie um programa que leia uma formula e diga se é valida em relação aos parentes
# l = str(input('Digite sua formula:'))
# e = x = 0
# for c in range(0, len(l)):
#     if e == 0:
#         if "(" == l[c]:
#             e += 1
#     elif ")" == l[c]:
#         e -= 1
# if e == 0:
#     print("Esta operação é valida.")
# else:
#     print("Esta operação não é valida.")

e = str(input('Digite sua formula:'))
p = []
for s in e:
    if s == "(":
        p.append("(")
    elif s == ")":
        if len(p) > 0:
            p.pop()
        else:
            p.append(")")
            break
if len(p) == 0:
    print('Sua expressao esta valida')
else:
    print('Sua expressao esta errada')
