from time import sleep
from cores import cor

valor1 = int(input('{}Primeiro valor: {}'.format(cor['amarelo'], cor['final'])))
valor2 = int (input('{}Segundo valor: {}'.format(cor['amarelo'], cor['final'])))
key =  0
t = 1
while key != 5:
    sleep(t)
    print('{}{}{}'.format(cor['vermelho'],(13*'-='+'-'),cor['final']))
    print('''    {}[ 1 ] Somar 
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa
    [ 6 ] Velocidade{}'''.format(cor['roxo'], cor['final']))
    n = int(input('{}O que deseja fazer? {}'.format(cor['azul'],cor['final'])))

    if n == 1:
        soma = valor1 + valor2
        print(f'>>>>> {valor1} + {valor2} = {soma}')
    elif n == 2:
        mult = valor1 * valor2
        print(f'>>>>> {valor1} x {valor2} = {mult}')
    elif n == 3:
        if valor1 > valor2:
            maior = valor1
        else:
            maior = valor2
        print(f'>>>>> Entre {valor1} e {valor2} o maior é {maior}.')
    elif n == 4:
        valor1 = int(input('{}Primeiro valor: {}'.format(cor['amarelo'], cor['final'])))
        valor2 = int (input('{}Segundo valor: {}'.format(cor['amarelo'], cor['final'])))

    elif n == 5:
        key = 5
        print('Finalizando...')
        sleep(2)
        print('Programa finalizado com sucesso.')
    
    elif n == 6:
        t = float(input("Mudar velocidade(1 a 10): "))

    else:
        n = print('Valor inválido. Digite novamente: ')
