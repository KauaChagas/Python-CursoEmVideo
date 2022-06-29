nome = input('Digite o nome complete: ').strip()
nome = nome.lower()
a = nome.count('a')
posição1 = nome.find('a')
posição2 = nome.rfind('a')

print(f'Quatidade de "a": {a}\nPosição do Primeiro a: {posição1+1}\nPosição do ultimo a: {posição2+1}')
