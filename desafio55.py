lista = []
print(f"{10*'-'}DIGITE O PESO EM QUILOGRAMAS(kg){10*'-'}")
for i in range(1, 6):
    peso = float(input(f"Peso da {i}º pessoa: "))
    lista.append(peso)
    lista.sort()

print(f"O maior peso inserido foi {lista[-1]:.0f}kg.\nO menor peso digitado foi {lista[0]:.0f}kg.")
# =========OUTRA FORMA DE RESOLVER========
# maior = 0
# menor = 0
# for i in range(1,6):
#     peso = float(input(f"Peso da {i}º pessoa: "))

#     if i == 1:
#         maior = peso
#         menor = peso

#     if maior < peso:
#         maior = peso

#     elif menor > peso:
#         menor = peso
    
# print(f"O maior peso inserido foi de {maior:.2f}kg")
# print(f"O menor peso inserido foi de {menor:.2f}")