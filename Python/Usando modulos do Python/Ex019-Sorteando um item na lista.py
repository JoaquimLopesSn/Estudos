from random import choice
al1 = str(input('Primeiro aluno: '))
al2 = str(input('Segundo aluno: '))
al3 = str(input('terceiro aluno: '))
al4 = str(input('quarto aluno: '))

lista = [al1, al2, al3, al4]
ram = choice (lista)
print ('O aluno que ira apagar o quadro sera: {}'.format(ram))
