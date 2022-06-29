from random import randint
from time import sleep
print('''Suas opções:
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura''')
 
jogada = int(input('Qual a sua jogada? '))

if jogada > 3:
    print("Valor inválido.")

else:
    cyber = randint(1,3)
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')
    sleep(1)
    
    if jogada == 1 and cyber == 3:
        print('-='*10+'-')
        print(f'Cyber jogou TESOURA\nJogador jogou PEDRA')
        print('-='*10+'-')
        print('JOGADOR VENCE!')

    elif jogada == 2 and cyber == 1:
        print('-='*10+'-')
        print(f'Cyber jogou PEDRA\nJogador jogou PAPEL')
        print('-='*10+'-')
        print('JOGADOR VENCE!')

    elif jogada == 3 and cyber == 2:
        print('-='*10+'-')
        print(f'Cyber jogou PAPEL\nJogador jogou TESOURA')
        print('-='*10+'-')
        print('JOGADOR VENCE!')

    elif cyber == 1 and jogada == 3:
        print('-='*10+'-')
        print(f'Cyber jogou PEDRA\nJogador jogou TESOURA')
        print('-='*10+'-')
        print('CYBER VENCE!')

    elif cyber == 2 and jogada == 1:
        print('-='*10+'-')
        print(f'Cyber jogou PAPEL\nJogador jogou PEDRA')
        print('-='*10+'-')
        print('CYBER VENCE!')

    elif cyber == 3 and jogada == 2:
        print('-='*10+'-')
        print(f'Cyber jogou TESOURA\nJogador jogou PAPEL')
        print('-='*10+'-')
        print('CYBER VENCE!')

    else:
        if cyber == 1:
            p = 'PEDRA'

        elif cyber == 2:
            p = 'PAPEL'

        elif cyber == 3:
            p = 'TESOURA'
        print('-='*10+'-')
        print(f'Cyber jogou {p}\nJogador jogou {p}')
        print('-='*10+'-')
        print('EMPATE.')

