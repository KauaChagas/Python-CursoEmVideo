s = 0
c = -1
num = 0
while num != 999:
    s += num
    num = int(input("Digite um número[999 para parar]: "))
    c += 1
    
print(f"A soma dos {c} números digitados é {s}")