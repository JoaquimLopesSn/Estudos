valor = float(input('Preço das compras: R$'))

print('''
FORMAS DE PAGAMENTO
[ 1 ] À vista dinheiro/cheque
[ 2 ] À vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão                
''')
op = int(input('Qual é a opção? '))

if op == 1:
    valorop = valor - ((valor * 10) / 100)
    print('Sua compra de R${:.2f} com desconto de 10%, vai custar R${:.2f} no final.'.format(valor, valorop))
elif op == 2:
    valorop = valor - ((valor * 5) / 100)
    print('Sua compra de R${:.2f} com desconto de 5%, vai custar R${:.2f} no final.'.format(valor, valorop))
elif  op == 3:
    valorop = valor / 2
    print('Sua compra de R${:.2f} vai gerar 2x parcelas de R${:.2f}'.format(valor, valorop))
elif op == 4:
    parcelas = int(input('Quantas parcelas? '))
    valorop = valor + ((valor * 20) / 100)
    print('Sua compra de R${:.2f} vai gerar {}x parcelas de R${:.2f}'.format(valor, parcelas, (valorop / parcelas)))
