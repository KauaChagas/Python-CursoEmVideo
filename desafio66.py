cont = soma = 0

while True:
    num = int(input('Digite um número(999 para encerrar): '))
    if num == 999:
        break
    soma += num
    cont += 1

print(f"A soma dos {cont} números digitados é {soma}.")
