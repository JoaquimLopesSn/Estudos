from random import choice

jogador =  int(input('''\033[1;32m                
                I=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-I
                I                                                I
                I     Bem Vindo ao jogo PEDRA, PAPEL E TESOURA   I
                I                                                I
                I                [ 1 ] PEDRA                     I
                I                [ 2 ] PAPEL                     I
                I                [ 3 ] TESOURA                   I
                I                                                I
                I=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-I
                     
Digite o numero da jogada:   '''))
print("                        ")
print("                        ")


lista = (1, 2, 3)

pc = choice(lista)
print('\033[1;32mresposta pc: {}'.format(pc))
print('\033[1;32mresposta jogador: {}'.format(jogador))

print("                        ")
print('          JO')
print('          KEN')
print('          PO!!!')
print("                        ")

if pc == 1 and jogador == 1:
    print('''    Você	 Máquina
    ____	 ____
  _/  _ \\      _/    \\
 / _ - _ \\    / _ - _ \\
 \\_______/    \\_______/ 

   ┌─┐┌┬┐┌─┐┌─┐┌┬┐┌─┐ 
   ├┤ │││├─┘├─┤ │ ├┤  
   └─┘┴ ┴┴  ┴ ┴ ┴ └─┘ ''')
elif pc == 2 and jogador == 1:
    print('''     Você	 Máquina
    ____	  _____
  _/  _ \\        O_____O
 / _ - _ \\       /     /
 \\_______/      /____ /
               O_____O
                   
   ┌─┐┌─┐┬─┐┌┬┐┌─┐┬ ┬ 
   ├─┘├┤ ├┬┘ ││├┤ │ │ 
   ┴  └─┘┴└──┴┘└─┘└─┘ ''')
elif pc == 3 and jogador == 1:
    print('''    Você	 Máquina
                  _    _
    ____         (_)  / )
  _/  _ \\          | (_/ 
 / _ - _ \\        _+/  
 \\_______/       //|\\
                // ||
               (/  |/ 

   ┬  ┬┌─┐┌┐┌┌─┐┌─┐┬ ┬
   └┐┌┘├┤ ││││  ├┤ │ │
    └┘ └─┘┘└┘└─┘└─┘└─┘''')
elif pc == 1 and jogador == 2:
    print('''     Você	 Máquina
    _____         ____
   O_____O      _/  _ \\
   /     /     / _ - _ \\
  /____ /      \\_______/
 O_____O

   ┬  ┬┌─┐┌┐┌┌─┐┌─┐┬ ┬
   └┐┌┘├┤ ││││  ├┤ │ │
    └┘ └─┘┘└┘└─┘└─┘└─┘
''')
elif pc == 2 and jogador == 2:
    print('''     Você	 Máquina
    _____         _____
   O_____O       O_____O
   /     /       /     /
  /____ /       /____ /
 O_____O       O_____O

   ┌─┐┌┬┐┌─┐┌─┐┌┬┐┌─┐ 
   ├┤ │││├─┘├─┤ │ ├┤  
   └─┘┴ ┴┴  ┴ ┴ ┴ └─┘ 
''')
elif pc == 3 and jogador == 2:
    print('''     Você	 Máquina
                  _    _
    _____        (_)  / )
   O_____O         | (_/
   /     /        _+/
  /____ /        //|\\
 O_____O        // ||
               (/  |/

   ┌─┐┌─┐┬─┐┌┬┐┌─┐┬ ┬ 
   ├─┘├┤ ├┬┘ ││├┤ │ │ 
   ┴  └─┘┴└──┴┘└─┘└─┘''')
elif pc == 1 and jogador == 3:
    print('''     Você	 Máquina
    _    _
   (_)  / )       ____
     | (_/      _/  _ \\
    _+/        / _ - _ \\
   //|\        \\_______/
  // ||
 (/  |/ 

   ┌─┐┌─┐┬─┐┌┬┐┌─┐┬ ┬ 
   ├─┘├┤ ├┬┘ ││├┤ │ │ 
   ┴  └─┘┴└──┴┘└─┘└─┘
''')
elif pc == 2 and jogador == 3:
    print('''     Você	 Máquina
    _    _
   (_)  / )       _____
     | (_/       O_____O
    _+/          /     /
   //|\         /____ /
  // ||        O_____O
 (/  |/ 

   ┬  ┬┌─┐┌┐┌┌─┐┌─┐┬ ┬
   └┐┌┘├┤ ││││  ├┤ │ │
    └┘ └─┘┘└┘└─┘└─┘└─┘
''')
elif pc == 3 and jogador == 3:
    print('''     Você	 Máquina
    _    _       _    _
   (_)  / )     (_)  / )
     | (_/        | (_/
    _+/          _+/
   //|\\         //|\\
  // ||        // ||
 (/  |/       (/  |/

   ┌─┐┌┬┐┌─┐┌─┐┌┬┐┌─┐ 
   ├┤ │││├─┘├─┤ │ ├┤  
   └─┘┴ ┴┴  ┴ ┴ ┴ └─┘ ''')
    