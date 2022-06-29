lado1 = int(input('Lado 1: '))
lado2 = int(input('Lado 2: '))
lado3 = int(input('Lado 3: '))

if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado3 + lado2 > lado1):
    if lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print('Triângulo ISÓSCELES.')

    elif lado1 == lado2 == lado3:
        print('Triângulo EQUILÁTERO.')

    elif lado1 != lado2 != lado3:
        print('Triângulo ESCALENO.')

else:
    print('O triângulo não pode ser formado.')