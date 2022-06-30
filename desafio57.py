sexo =  str(input('Digite seu sexo[M/F]: ')).strip().upper()

while sexo not in 'MF':
    sexo = input('Valor inválido. Digite novamente: ').strip().upper()
    
if sexo == 'F':    
    print(f'Sexo feminino registrado com sucesso!')

else:
    print(f'Sexo masculino resgistrado com sucesso!')