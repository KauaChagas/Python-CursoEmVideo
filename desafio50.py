v1 = int(input("Primeiro valor: "))
v2 = int(input("Segundo valor: "))
v3 = int(input("Terceiro valor: "))
v4 = int(input("Quarto valor: "))
v5 = int(input("Quinto valor: "))
v6 = int(input("Sexto valor: "))

lista = [v1, v2, v3, v4, v5, v6]
VD = []
soma = 0
for i in lista:
    if i%2 == 0:
        soma += i

    else:
        VD.append(i)

print(f"Soma dos números pares: {soma}.\nValores desprezados: {VD}.")

# =========OUTRA FORMA DE RESOLVER=========

# soma = 0
# cont = 0
# lista = []
# for i in range(1, 7):
#     valor = int(input("Digte o {}º valor: ".format(i)))
#     if valor%2 == 0:
#         soma += valor
#     else:
#         cont += 1
#         lista.append(valor)

# print("A soma dos valores pares é {}.".format(soma))
# print("Foram desprezados {} valores: {}.".format(cont, lista))