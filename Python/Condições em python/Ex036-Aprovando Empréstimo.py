print ('Olá, para consultar se havera aprovação do emprestimo, digite as seguintes informações solicitadas abaixo.')

valorcasa = int(input('Qual e o valor do imóvel: R$'))
salario = int(input('Qual e seu atual salario: R$'))
tempo = int(input('Quantos anos de financiamento vc deseja: '))


parcela = valorcasa // (tempo*12)

sal30 = ((salario * 30) / 100)

aprovado = parcela <= sal30

if parcela <= sal30:
    print('Seu financiamento foi APROVADO e sua parcela sera R${}.'.format(parcela))
else:
    print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}, sendo assim o empréstimo foi NEGADO!'.format(valorcasa, tempo, parcela))
