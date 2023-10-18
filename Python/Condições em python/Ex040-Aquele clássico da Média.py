print('Ola Esse programa tem como objetivo calcular notas dos 4 bimestres de um aluno!')
n1 = float(input('Digite ano ta do 1° Bimestre: '))
n2 = float(input('Digite ano ta do 2° Bimestre: '))
n3 = float(input('Digite ano ta do 3° Bimestre: '))
n4 = float(input('Digite ano ta do 4° Bimestre: '))

nota = (n1+n2+n3+n4) / 4

if nota < 5.0:
    print('O aluno foi REPROVADO!!!')
elif nota < 6.9: 
    print('O aluno esta de RECUPERAÇÂO!!!')
else:
    print('O aluno foi APROVADO!!!')
print('E sua nota e {:.2f}'.format(nota))