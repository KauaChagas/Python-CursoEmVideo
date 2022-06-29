numero = int(input('Digite um número'))
m = numero//1000
numero %= 1000
c = numero//100
numero %= 100
d = numero//10
numero %= 10
u = numero//1

print(f'Milhar:{m}\nCentena:{c}\nDezena:{d}\nUnidade:{u}')