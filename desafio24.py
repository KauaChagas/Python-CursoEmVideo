cidade = input('Digite o nome da cidade: ')
cidade = cidade.lower()
cidade = cidade.split()

if cidade[0] == 'santo':
    print('sim')

else:
    print('não')

# OUTRA FOMRA DE RESOLVER ---> print(cidade[:5].lower() == 'santo')