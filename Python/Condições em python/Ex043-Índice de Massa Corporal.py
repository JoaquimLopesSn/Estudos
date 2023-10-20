peso = float(input('Qual e seu peso? (kg) '))
altura = float(input('Qual e sua altura? (m) '))

imc = peso / (altura * altura)

print('O IMC dessa pessoa é de {:.2F}'.format(imc))

if imc < 18.5:
    print('Voçe esta abaixo do ABAIXO DO PESO normal')
elif imc <= 25:
    print('PARABÉNS, voçe está na faixa de PESO NORMAL')
elif imc <= 30:
    print('Voçe esta em SOBREPESO')
elif imc <= 40:
    print('Voçe esta em OBESIDADE')
elif imc > 40:
    print('CUIDADO, Voçe esta em OBESIDADE MÓRBIDA')