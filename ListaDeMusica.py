from random import choice
lista = ['tarcisio', 'joao gomes', 'Vitor fernandes', 'felipe amorim', 'akon', 'dodo pressão']

f = len(lista)
c = 0

while c != f:
    e = choice(lista)
    print(e)
    lista.remove(e)
    c += 1

print("não há mais músicas.")
