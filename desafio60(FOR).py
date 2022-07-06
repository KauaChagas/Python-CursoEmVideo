num = int(input("Descubra o fatorial: "))
cont = 0
f = 1
print(f'{num}! = ',end='')
for i in range(num):
    cont += 1
    f *= cont
    print(f'{cont}',end='')
    print(f' x ' if cont<num else ' = ', end='')

print(f)
    