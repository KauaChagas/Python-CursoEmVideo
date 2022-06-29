nome = input('Digite o nome completo: ')
nome = nome.lower()
nome = nome.find('silva')

if nome >= 0:
    print('Tem!')

else:
    print('Não tem.')


# '''----------1. OUTRA FORMA DE RESOLVER 1.----------'''
# nome = input('Digite o nome completo: ').lower()
# encontrar = nome.find('silva')

# print(encontrar > 0)

# '''----------2. OUTRA FORMA DE RESOLVER 2.----------'''
# print('silva' in nome.lower())



