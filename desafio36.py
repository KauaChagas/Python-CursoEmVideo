casa = int(input("Valor da casa: "))
salario = float(input("Digite seu salário: "))
anos = int(input("Duração: "))

meses = anos * 12
prestacao = casa / meses
limite = salario * 0.3

if prestacao > limite:
    print("Empréstimo negado.")

else:
    print("A casa é sua, so pagar agora :)", end=" ")

print("--Construtora KR--")
