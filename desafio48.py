valor = int(input("Digite o número: "))

soma = 0

for i in range(0, valor+1):
    if i%2 != 0:
        if i%3 == 0 and 1<= i <= 500:
            soma += i

print(soma)
