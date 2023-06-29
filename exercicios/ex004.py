u = input('Escreva algo:')

print('Seu tipo primitivo é:',type(u))
print('O que vc escreveu e um numero:',u.isnumeric())
print('O que vc escreveu contem letras:',u.isalpha())
print('O que vc escreveu e alfanumerico:',u.isalnum())
print('O que vc escreveu tem espaços:',u.isspace())