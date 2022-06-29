from random import choice

tentativa = int(input('Tente advinha o número oculto de 0 a 5: \n'))
lista = [1,2,3,4,5]
numero = choice(lista)

if tentativa == numero:
    print(f'Parebénssss, você acertou!!!!!\n{15*"-"}O numero oculto era {numero}{15*"-"}.')

else:
    print('Você errou :(\nO computador venceu.')


print(f'{numero*"-"}Fim do jogo{numero*"-"}')


