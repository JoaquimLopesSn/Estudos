numero = int(input('Digite um numero qualquer: '))
div = numero % 2    #resto da divisao de numero por 2.  se for impar da 1 se par da 0
 
if div == 0: 
    print('O numero {} é PAR'.format(numero))
else:
    print('O numero {} é ÍMPAR'.format(numero))

