from datetime import date

atual = date.today().year

nascimento = int(input('Ano de nascimento: '))

idade = atual - nascimento

print(f'O atleta possui {idade} anos. Portanto:')
if 4 < idade <= 9:
    print('Sua categoria é MIRIM.')

elif 9 < idade <= 14:
    print('Sua categoria é INFANTIL.')

elif 14 < idade <= 19:
    print('Sua categoria é JUNIOR.')

elif 19 < idade <= 25:
    print('Sua categoria é SÊNIOR.')

elif idade > 25: 
    print('Sua categoria é MASTER.')
