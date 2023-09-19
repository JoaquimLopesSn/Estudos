distancia = float(input('Qual e a distância da sua viagem? '))

print('Você esta prestes a começar uma viagem de {}Km'.format(distancia))
"""p1 = distancia * 0.50 
p2 = distancia * 0.45
if distancia > 200:
    print('O preço da sua viagem será de R${:.2f}'.format(p2))
else:
    print('O preço da sua viagem será de R${:.2f}'.format(p1))"""
#foi o que eu fiz 
if distancia <= 200:
    preço = distancia * 0.50 
else:
    preço = distancia * 0.45 
print('O preço da sua viagem será de R${:.2f}'.format(preço))

#foi o professor 