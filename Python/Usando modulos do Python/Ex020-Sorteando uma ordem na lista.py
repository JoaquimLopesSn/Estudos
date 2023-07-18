from random import sample

al1 = str(input('Primeiro aluno: '))
al2 = str(input('Segundo aluno: '))
al3 = str(input('Terceiro aluno: '))
al4 = str(input('Quarto aluno: '))

lista = (al1, al2, al3, al4)

print ('A lista aleatoria de alunos que vão apresentar o trabalho e: {}'.format (sample (lista, 4)))
