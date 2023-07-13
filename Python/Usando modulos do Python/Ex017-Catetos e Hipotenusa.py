'''co = float(input("Cumprimento do cateto oposto: "))
ca = float(input("Cumprimento do cateto adjacente: "))

hi = (((co*co)+(ca*ca))**(1/2))

print ("A hipotenusa vai medir {:.2f}".format(hi))'''

import math
co = float(input("Cumprimento do cateto oposto: "))
ca = float(input("Cumprimento do cateto adjacente: "))

hi = math.hypot (co, ca)

print ("A hipotenusa vai medir {:.2f}".format(hi))