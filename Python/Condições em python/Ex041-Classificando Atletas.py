from datetime import date

at = int(input('Digite o ano de nascimento do atleta: '))

atual = date.today().year

idade = atual - at

if idade <= 9:
    print('Com {} anos a categoria do atleta e MIRIM.'.format(idade))
elif idade <= 14:
    print('Com {} anos a categoria do atleta e INFANTIL.'.format(idade))
elif idade <= 19:
    print('Com {} anos a categoria do atleta e JÚNIOR.'.format(idade))
elif idade <= 25:
    print('Com {} anos a categoria do atleta e SÊNIOR.'.format(idade))
else:
    print('Com {} anos a categoria do atleta e MASTER.'.format(idade))