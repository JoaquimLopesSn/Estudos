import random

print ('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print ('                         Vou Pensar em um número entre 0 e 5. tente adivinhar...')
print ('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

ni = int(input('Em qual número eu pensei? '))
no = random.randint(0, 5)

if ni == no: 
   print('PARABENS VC ACERTOU')
else:
   print('ERROU, o numero que pensei foi {}'.format(no))