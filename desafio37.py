numero = int(input('Digite um número inteiro: '))
conversão = int(input("Qual será sua medida de conversão?\n[1]Octal\n[2]Binário\n[3]Hexadecimal"))

if conversão == 1:
    print(f'O número {numero} em Octal é: {oct(numero)}')

elif conversão == 2:
    print(f'O número {numero} em binário é: {bin(numero)}')

elif conversão == 3:
    print(f'O número {numero} em hexadecimal é: {hex(numero)}')

else:
    print('Você fez alguma coisa de errado!')