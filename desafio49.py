valor = int(input("Digite um número: "))

print(f"{15*'='}TABUADA DO {valor}{15*'='}")
for i in range(11):
    
    print(f"{valor} x {i} = {valor*i}")