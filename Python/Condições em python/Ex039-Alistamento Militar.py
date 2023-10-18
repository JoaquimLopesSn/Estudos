from datetime import date

atual = date.today().year
nasc = int(input('Ano de nascimento: '))
print('''Qual e seu genero: 
[1] Homen
[2] Mulher ''')
genero = int(input('Voçe e homen ou mulher: '))
idade = atual-nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc,idade,atual))

if genero == 1 :
    if (idade) < 18:
        print('''Ainda falta {} anos para seu alistamento.
    Seu alistamento será em {}'''.format((18-idade), atual+(18-idade)))
    elif (idade) > 18:
        print('''Voçe ja deveria ter se alistado há {} anos.
    Seu alistamento foi em {}'''.format((idade-18), atual-(idade-18)))
    elif idade == 18:
        print('Voçe deve se alistar IMEDIATAMENTE!')
else:
    print('Seu alistamento não e obrigatorio.')


