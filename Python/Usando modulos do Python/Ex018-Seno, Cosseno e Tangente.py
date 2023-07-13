import math
ang = float(input('Digite o ângulo que voçe deseja: '))
rad = math.radians(ang)
se = math.sin(rad)
cos = math.cos(rad)
tan = math.tan(rad)

print('O angulo de {} tem o SENO de {:.2f}'.format(ang,se))
print('O angulo de {} tem o COSSENO de {:.2f}'.format(ang,cos))
print('O angulo de {} tem o TANGENTE de {:.2f}'.format(ang,tan))
