salario = float(input('Digite o salário do funcionário: '))

if salario <= 1250:
    aumento = salario * 0.15
    sf = salario + aumento
    print(f'Você teve um aumento de 10% equivalente a {aumento} reais do seu salário!!!\nSeu salário agora é: {sf}')

elif salario > 1250:
    aumento = salario * 0.1
    sf = salario + aumento
    print(f'Você teve um aumento de 15% equivalente a {aumento} reais do seu salário!!!\nSeu salário agora é: {sf}')