print(f'{10*"-"}SEQUÊNCIA DE FICBONACCI{10*"-"}')
t = int(input("Quantos termos você deseja? "))
c = 0
f1 = 0
f2 = 1

while c < t:
    c += 1
    print(f1,end='') 
    f = f1+f2
    f1 = f2
    f2 = f
    
    print(" → " if c<t else " → ",end='')

print('FIM')


    
