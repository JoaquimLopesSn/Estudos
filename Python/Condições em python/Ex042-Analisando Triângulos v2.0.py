print('-='*40)
print('Analisador de Triângulos')
print('-='*40)
l1 = float(input('Primeiro segmento: '))
print('-='*40)
l2 = float(input('Segundo segmento: '))
print('-='*40)
l3 = float(input('Terceiro segmento: '))
print('-='*40)

if (l1 + l2) > l3 and (l1 + l3) > l2 and (l2 + l3) > l1:
    print('O segmentos PODEM FORMAR um triângulo ',end='')
    if l1 == l2 == l3:
        print('EQUILÁTERO!')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('ISÓSCELES!')
    elif l1 != l2 != l3:
        print('ESCALENO!')
else:
    print('O segmentos NÃO PODEM FORMAR um triângulo.')
print('-='*40)