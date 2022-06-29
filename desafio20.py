import random
a1 = input('Primeiro aluno(a): ')
a2 = input('Segundo aluno(a): ')
a3 = input('Terceiro aluno(a): ')
a4 = input('Quarto aluno(a): ')

lista = [a1, a2, a3, a4]
random.shuffle(lista)

print(lista)
