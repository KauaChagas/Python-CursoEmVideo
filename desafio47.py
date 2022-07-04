# numero = int(input('Digite um número: '))
# lista = []
# for i in range(1, numero+1):
#     if i % 2 == 0:
#         lista.append(i)
# lista.append('acabou')
# print(lista)


#=========OUTRA FORMA DE RESOLVER=========
num = int(input('Digite um número: '))

for i in range(2, num + 1, 2):
    print(i,end=' ')

print('acabou')
