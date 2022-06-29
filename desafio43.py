altura = float(input('Digite sua altura: '))/100
peso = float(input('Digite seu peso: '))

imc = peso / (altura**2)
imc = round(imc,1)
if imc < 18.5:
    print(f'Seu IMC: {imc}.\nVocê está abaixo do peso.')

elif 18.5 < imc <= 25:
    print(f'Seu IMC: {imc}.\nVocê está com o peso ideal.')

elif 25 < imc <= 30:
    print(f'Seu IMC: {imc}.\nVocê está a cima do peso ideial.')

elif 30 < imc <= 40:
    print(f'Seu IMC: {imc}.\nVocê está obeso.')

elif imc > 40:
    print(f'Seu IMC: {imc}.\nVocê chegou no estágio de obesidade mórbita.') 