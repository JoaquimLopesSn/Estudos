sal = float(input('Digite o valor do salario que vc recebe agora: '))


if sal <= 1250: 
    salnovo = ((sal * 15) / 100) + sal #formula de porcentagem 
else:
    salnovo = ((sal * 10) / 100) + sal

print('Quem recebia R${:.2f} agora recebera R${:.2f}.'.format(sal, salnovo))