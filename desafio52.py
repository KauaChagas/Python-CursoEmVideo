num = int(input("Digite um número e descubra se ele é primo: "))
lista = []

for i in range(1, num+1):
    if num%i == 0:
        i = str(i)
        lista.append(i)

print(lista)

if len(lista) > 2:
    print(f"O número {num} não é primo.")

else:
    if lista[0] == '1' and lista[1] == str(num):
        print(f"O número {num} é primo!")

    else:
        (f'O número {num} não é primo.')