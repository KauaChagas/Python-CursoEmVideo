l = 's'
c = 0
s = 0
m = 0
n = 0

while l in 'Ss':
    v = int(input('Digite um valor: '))
    c += 1
    s += v
    if c == 1:
        m = n = v
    else:
        if v > m:
            m = v
        elif v < n:
            n = v
    l = str(input('Deseja continuar?[S/N]:')).strip()

print(f'Você digitou {c} números e a média foi {s/c}')
print(f'Maior:{m}\nMenor:{n}')