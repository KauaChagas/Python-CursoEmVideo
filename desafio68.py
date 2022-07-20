from random import randint
c = 0
while True:
    print('-='*10+'-')
    comp = randint(1,10)
    valor = int(input('Digite seu número: '))
    e = input('Par ou Impar?[P/I] ')
    soma = comp + valor

    if soma%2 == 0 and e in 'Pp':
        print('-'*20)
        print(f'Computador x Você\n{comp: ^11}+ {valor: ^5} = {soma}')
        print(f'{soma} é par. Você VENCEU!!!')
        c += 1

    elif soma%2 != 0 and e in 'Ii':
        print('-'*20)
        print(f'Computador x Você\n{comp: ^11}+ {valor: ^5} = {soma}')
        print(f'{soma} é impar. Você VENCEU!!!')
        c += 1

    else:
        if e in 'Ii':
            print('-'*20)
            print(f'Computador x Você\n{comp: ^11}+ {valor: ^5} = {soma}')
            print(f'{soma} é par. Você PERDEU!!!')
            break

        elif e in 'Pp':
            print('-'*20)
            print(f'Computador x Você\n{comp: ^11}+ {valor: ^5} = {soma}')
            print(f'{soma} é ímpar. Você PERDEU!!!')
            break

print(f'Você venceu {c} vezes. GAME OVER!')