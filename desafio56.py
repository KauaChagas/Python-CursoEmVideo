idades = 0
contador = 0
maior = 0


for i in range(4):
    nome = str(input("Nome: "))
    idade = int(input("Idade: "))
    sexo = str(input("Sexo[M/F]: "))

    if sexo in 'Mm':
        if idade > maior:
            maior = idade
            oldMan = nome

        else:
            None

    if idade < 20 and sexo in 'Ff':#sera aceito o F ou f
        contador += 1

    idades += idade


media = idades/4

print(f'O homem mais velho do grupo se chama {oldMan}, com {maior} anos.')
print(f'A média da idade do grupo é {media:.0f} anos.')
print(f'Existe {contador} mulheres com menos de 20 anos.')