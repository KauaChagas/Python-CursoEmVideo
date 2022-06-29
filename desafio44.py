print(f'{10*"="}LOJAS KR{10*"="}') 
preco = float(input('Preço da compra: '))
print(f'''{15*'-'} FORMAS DE PAGAMENTO {15*'-'}
[ 1 ] À vista(DINHEIRO ou CHEQUE): 10% de DESCONTO.
[ 2 ] À vista(CARTÃO): 5% de DESCONTO.
[ 3 ] 2x no cartão.
[ 4 ] 3x ou mais no cartão: 20% de juros.''')

pagamento = int(input('Forma de pagamento escolhida: '))
if pagamento == 4:
    parcelas = int(input('Quantas parcelas? '))
    preco2 = (preco * 0.2) + preco
    valor = preco2 / parcelas
    
    print(f'Sua compra será parcelada em {parcelas} vezes de {valor:.2f} reais.\nSua compra de {preco:.2f} reais, ao final será {preco2:.2f} reais.')

elif pagamento == 3:
    print(f'Sua compra foi dividida em duas vezes sem juros.\nSerão duas parcelas de {preco/2:.2f} reais.')

elif pagamento == 2:
    preco1 = (preco * 0.05) - preco
    print(f'Você recebeu 5% de desconto!\nPortanto suas compras de {preco} reais baixaram para {preco1} reais.')

elif pagamento == 1:
    preco1 = (preco * 0.1) - preco
    print(f'Você recebeu 10% de desconto!!!.\nO valor a pagar agora é de {preco1} reais.')