n1 = float(input('Digite uma distância em metro:'))

km = n1 * 1000
hm = n1 * 100
dam = n1 * 10
dm = n1 / 10
cm = n1 / 100
mm = n1 / 1000

print('A medida de {:.1f} corresponde as seguintes unidades de medida:'.format(n1))
print('Quilômetro:',km,'km')
print('Hectômetro:',hm,'hm')
print('Decâmetro:',dam,'dam')
print('Metro:',n1,'m')
print('Decímetro:',dm,'dm')
print('Centímetro:',cm,'cm')
print('Milímetro:',mm,'mm')


