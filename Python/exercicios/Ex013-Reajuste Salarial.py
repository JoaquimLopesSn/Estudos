valor  = float(input("Qual é o salário do funcionário? R$"))
calculo = (valor+((valor*15)/100))
print("Um funcionário que ganhava R${:.2f}, com um aumento de 15%, passou a ganhar R${:.2f}.".format(valor, calculo))


