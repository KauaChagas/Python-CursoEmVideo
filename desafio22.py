nome = input('Digite seu nome completo: ')
Pnome = nome.split()
letras = ''.join(Pnome)

print(nome.lower())
print(nome.upper())
print(f'{len(letras)} -> {letras}')
print(f'{len(Pnome[0])} -> {Pnome[0]}')

# CONTAR SÓ AS LETRAS -> print(len(nome)- nome.count(' '))
