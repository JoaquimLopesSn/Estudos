print ('Sistema de calculo de notas')
n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1 + n2) / 2
print ('Sua media foi {:.1f}'.format(m))
if m >= 6.0:
    print('sua media foi boa! PARABÉNS VOÇE PASSOU')
else: 
    print('sua media foi RUIM! INFELIZMENTE VOÇE NÃO PASSOU')
