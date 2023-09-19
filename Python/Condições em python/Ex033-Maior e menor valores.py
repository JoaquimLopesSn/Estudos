a = int(input('Digite o primeiro numero: '))
b = int(input('Digite o segundo numero: '))
c = int(input('Digite o terceiro numero: '))
#condição menor
if a<b and a<c:
    menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
#condição maior 
if a>b and a>c:
    maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c



if a != menor and a != maior:
    meio = a
if b != menor and b != maior:
    meio = b
if c != menor and c != maior:
    meio = c


print ('O menor valor digitado e {} o ultimo e {} e o {} esta no meio dos dois.'.format(menor, maior, meio ))