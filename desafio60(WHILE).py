from cores import cor

num = int(input("Descubra o fatorial: "))
c = 0
f = 1
# -> SEM COR
print(f"==========[Fatorial de {num}]==========")
while c != num:
    c += 1
    f = c * f
    if c != num:
        print('{} x'.format(c),end=' ')
    else:
        print('{} = {}'.format(c, f))

# -> COM COR
# print(f"==========[{cor['vermelho']}Fatorial de {num}{cor['final']}]==========")
# while c != num:
#     c += 1
#     f = c * f
#     if c != num:
#         print('{}{}{} x'.format(cor['verde'],c, cor['final']),end=' ')
#     else:
#         print('{}{}{} = {}{}{}'.format(cor['verde'],c,cor['final'],cor['amarelo'],f,cor['final']))

