velocidade = int(input('Velocidade do carro: '))

if velocidade > 80:
    diferença = velocidade - 80
    multa = diferença * 7
    print(f'Você foi multado.\nValor da multa: {multa} reais')

elif velocidade == 80:
    print('Tenha cuidado, você passou no limite.')

else:
    print('Continue dirigindo bem!!!')