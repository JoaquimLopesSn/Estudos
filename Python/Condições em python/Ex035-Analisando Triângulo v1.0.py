print('-='*20)
print('Analisador de Triângulos')
print('-='*20)
l1 = float(input('Primeiro segmento: '))
print('-='*20)
l2 = float(input('Segundo segmento: '))
print('-='*20)
l3 = float(input('Terceiro segmento: '))
print('-='*20)

if (l1 + l2) > l3 and (l1 + l3) > l2 and (l2 + l3) > l1:
    print('O segmentos PODEM FORMAR um triângulo.')
else:
    print('O segmentos NÃO PODEM FORMAR um triângulo.')
print('-='*20)
1
