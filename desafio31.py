distancia = int(input('Digite a distância da sua viagem: '))

if distancia <= 200:
    custo = distancia * 0.5
    print(f'O custo da sua passagem é de {custo} reais.')

elif distancia > 200:
    custo = distancia * 0.45
    print(f'O custo da sua passagem é de {custo:.2} reais.')

