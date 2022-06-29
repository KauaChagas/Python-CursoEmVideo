from datetime import date
ano = date.today().year
mes = date.today().month
dia = date.today().day

a = int(input('Ano de nacimento: '))
idade = ano - a

if idade < 18:
    p1 = 'anos'
    p2 = 'Faltam'
    diferença = 18 - idade
    if diferença == 1:
        p1 = 'ano'
        p2 = 'Falta'
    print(f'{p2} {diferença} {p1} para se você se alistar.')

elif idade == 18:
    print('Você precisa se alistar IMEDIATAMENTE.')

elif idade > 18:
    p1 = 'anos'
    diferença = idade - 18
    if diferença == 1:
        p1 = 'ano'
    print(f'Você deveria ter se alistado à {diferença} {p1}.')

