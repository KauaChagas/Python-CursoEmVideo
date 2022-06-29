nome = input('Digite seu nome: ')
nome = nome.split()
primero = nome[0]
nome.reverse()
ultimo = nome[0]

print(f'Primeiro nome: {primero}')
print(f'Segundo nome: {ultimo}')


# '''----------OUTRA FORMA DE RESOLVER----------'''
# print(nome.split()[len(nome.split())-1])
# pede a posição do nome dentro da lista nome.split()