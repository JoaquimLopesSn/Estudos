nome = str(input('Digite seu nome: ')).strip() #strip elimina espaços ante e depois da frase

semesp = nome.replace(' ','')
dividido = nome.split()

print('Seu nome em maiúsculo é {}.'.format(nome.upper()))
print('Seu nome em minúsculo é {}.'.format(nome.lower()))
print('Seu nome tem {} letras.'.format(len(nome) - nome.count(' ')))
#print('Seu nome tem {} letras.'.format(semesp.__len__()))
print('Seu primeiro nome e {} e tem {} letras.'.format(dividido[0], len(dividido[0])))


