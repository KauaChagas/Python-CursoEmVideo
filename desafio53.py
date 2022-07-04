frase = str(input('Digite seu políndromo: ')).strip().lower()
frase = frase.split()
frase = ''.join(frase)
contrario = []

for i in frase: #--->for letra in range(len(frase)-1,-1,-1):
    contrario.append(i)
contrario.reverse()
contrario = ''.join(contrario)

if contrario == frase:
    print(f'Original: {frase}\nInverso:  {contrario}')
    print("É um palíndromo!!!")
else:
    print(f'Original: {frase}\nInverso:  {contrario}')
    print("Não é um palíndromo.")