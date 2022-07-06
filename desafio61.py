termo = int(input('Termo de início: '))
razao = int(input('Razão: '))
c = 0
pa = termo

print(termo,end=' → ')
while c < 15:
    c += 1
    pa = pa + razao

    print(pa,end=' → ')

print('FIM')

    
