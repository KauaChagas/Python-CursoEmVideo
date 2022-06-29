lista = []
print(f"{10*'-'}DIGITE O PESO EM QUILOGRAMAS(kg){10*'-'}")
for i in range(1, 6):
    peso = float(input(f"Peso da {i}º pessoa: "))
    lista.append(peso)
    lista.sort()

print(f"O maior peso inserido foi {lista[-1]:.0f}kg.\nO menor peso digitado foi {lista[0]:.0f}kg.")