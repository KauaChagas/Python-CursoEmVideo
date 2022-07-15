

while True:
    print(15*'*')
    num = int(input('Tabuada do: '))
    if num < 0:
        break
    for i in range(1,11):
        mult = num*i
        print(f'{num} x {i} = {mult}')

print('FIM')