termo = int(input('Termo da PA: '))
razao = int(input('Razão: '))
key = 56
c = 9
contagem = 1

print(termo,end=' → ')
while key != 0:
    for i in range(c):
        c += 1
        termo = termo+razao
        contagem += 1

        print(termo, end=' → ')
    key = 0
    print('PAUSA')
    key = c = int(input('Mostrar mais quantos termos? '))

print(f'Ao todo foram exibidos {contagem} termos.')

