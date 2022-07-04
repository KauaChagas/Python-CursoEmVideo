# num = int(input("É primo? "))
# lista = []

# for i in range(1, num+1):
#     if num%i == 0:
#         i = str(i)
#         lista.append(i)

# if len(lista) > 2:
#     print(f"O número {num} não é primo.")
    
# else:
#     if lista[0] == '1' and lista[1] == str(num):
#         print(f"O número {num} é primo!")

#     else:
#         print(f'O número {num} não é primo.')
from cores import cor
num = int(input("É primo? "))

cont = 0

for i in range(1, num+1):
    if num%i==0:
        print('{}{}{}'.format(cor['verde'], i, cor['final']),end=' ')
        cont += 1

    else:
        print('{}{}{}'.format(cor['vermelho'], i, cor['final']),end=' ')

if cont > 2:
    print(f'\nO número {num} não é primo.')

else:
    print(f'\nO número {num} é primo!')