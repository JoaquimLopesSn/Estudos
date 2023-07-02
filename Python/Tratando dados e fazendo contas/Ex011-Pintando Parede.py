l = float(input('Largura da parede:'))
a = float(input('Altura da parede:'))

m2 = l * a
t = m2 / 2

print('Sua parede tem a dimenção de {}x{} e sua área é de {}m²'.format(l, a, m2))
print('Para pintar essa parede, você precisará de {}l de tinta'.format(t))
