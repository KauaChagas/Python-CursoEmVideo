nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))

media = (nota1 + nota2)/2

if 0 > nota1 or nota1 > 10:
    print('Valores fora de escala. Notas de 0 a 10.')

elif 0 > nota2 or nota2 > 10:
    print('Valores fora de escala. Notas de 0 a 10.') 

elif 6 <= media < 7:
    print(f'Eita, passou se arrastando hein. Média = {media}')

elif media < 6:
    print(f'Você está reprovado. Sua média: {media}')

else:
    print(f'Parabéns! Você foi aprovado com a média: {media}')