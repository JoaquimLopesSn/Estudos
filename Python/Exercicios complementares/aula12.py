
# if  >  SE
# elif > SENÂO SE
# else > ELSE


nome = str(input('Qual e seu nome? ')).capitalize()
if nome == 'Gustavo':
    print('Que nome bonito voçe tem!!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome e bem popular no Brasil.')
elif nome == 'Joaquim':
    print('Seu nome e o mais bonito do Brasil !!')
else:
    print('Seu nome e bem normal.')
print('tenha um bom dia, {} !'.format(nome))

