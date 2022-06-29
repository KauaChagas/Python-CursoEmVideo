l1 = int(input('Lado 1: '))
l2 = int(input('Lado 2: '))
l3 = int(input('Lado 3: '))

if (l1 + l2 > l3) and (l1 + l3 > l2) and (l3 + l2 > l1):
    print('É possível um triângulo com tais medidas!')

else:
    print('Não será possível formar um triângulo com tais medidas.')