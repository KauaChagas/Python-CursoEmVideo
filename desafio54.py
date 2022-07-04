# c = 0
# c2 = 0

# for i in range(1,8):
#     idade = int(input(f"Digite a {i}º idade: "))
#     if idade >= 21:
#         c += 1

#     else:
#         c2 += 1


# print(f"{c2} pessoas ainda não atingiram a maioridade.\nPorém {c} pessoas já atigiram a maioridade.")
from datetime import date
atual = date.today().year
maioridade = 0
menoridade = 0

for i in range(1,8):
    ano = int(input(f"[{i}ª pessoa] Digite o ano do seu nascimento: "))
    if (atual - ano ) >= 21:
        maioridade += 1
    else:
        menoridade += 1

print(f"{maioridade} pessoas atingiram a maioridade.")
print(f"Ao todo {menoridade} pessoas não atigiram.")