ano = int(input('Digite umn ano: '))
a = ano - 2020

if a > 0:
    a *= (-1)

if a % 4 == 0:
    print('É um ano bissexto!!')

else:
    print('Não é um ano bissexto :(')
    