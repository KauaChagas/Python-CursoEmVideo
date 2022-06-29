c = 0
c2 = 0

for i in range(1,8):
    idade = int(input(f"Digite a idade {i}: "))
    if idade >= 21:
        c += 1

    else:
        c2 += 1


print(f"{c2} pessoas ainda não atingiram a maioridade.\nPorém {c} pessoas já atigiram a maioridade.")