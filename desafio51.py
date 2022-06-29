primeiroTermo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))

c = primeiroTermo
print(primeiroTermo, end=" ")

for i in range(10):
    c += razao
    print(c, end=" ")