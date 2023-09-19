velociade = int(input('Em uma via 80km/h, qual a sua velocidade: '))

multa = (velociade - 80)* 7

#if velociade <= 80:
    #print('Tenha um bom dia! Dirija com segurança!')
#else:
    #print("MULTADO! você excedeu o limite permitido que é de 80km/h")
    #print('Você deve pagar uma multa de R${:.2f}'.format(multa))
    #print('Tenha um bom dia! Dirija com segurança!')
# isso foi o que eu fiz

if velociade > 80:
    print("MULTADO! você excedeu o limite permitido que é de 80km/h")
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')

# isso foi o que o professor fez