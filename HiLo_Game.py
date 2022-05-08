import  random

name = input("Por favor ingrese su nombre: ")

puntos = 300

primera_carta = 0
segunda_carta = 0

play = 'y'

while play.lower() == 'y':
    primera_carta = random.randint(1,13)
    segunda_carta = random.randint(1,13)
    print(f'\nThe first card is: {primera_carta}')
    opcion = input(f'{name}, la proxima carta es mas alta o baja (h o l): ')
    print(f'The next card is: {segunda_carta}')
    if primera_carta < segunda_carta and opcion.lower() == 'h':
        puntos += 100
        print(f'Won. Your score {name} is {puntos}')
    elif primera_carta > segunda_carta and opcion.lower() == 'l':
        puntos += 100
        print(f'Won. Your score is {puntos}')
    elif primera_carta == segunda_carta:
        print(f'Cards are the same. Your score is {puntos}')
    else:
        puntos -= 75 
        print(f'Lost. Your score is {puntos}')   
    if puntos <= 0:
        print(f'You lost. The end. Your score is {puntos}')
        play = 'n'
    else:    
        play = input(f'{name} want play again (y/n): ')
        if play.lower() != 'y':
           print(f'Thank you for playing. The final score is {puntos}\n.') 