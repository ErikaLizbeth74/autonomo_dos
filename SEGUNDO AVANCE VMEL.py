import random

print('\n\n\n\n')
print('=' * 75)
print('                   BIENVENIDO AL JUEGO DEL AHORCADO     ')
print('=' * 75)
print('\n\n')
print('=' * 75)
print('                          REGLAS DEL JUEGO')
print('\n')
print('      Adivinar una palabra en el menor número de intentos posibles')
print('                     Tienes 6 intentos para ganar')
print('Primero se deben marcar tantas rayas como letras tenga la palabra pensada.')
print('   Los jugadores tendrán que ir diciendo letras para formar la palabra')
print('        Se dibuja una horca y los jugadores van diciendo letras.')
print('       Si aciertan se escribe la letra en la raya que corresponda.')
print('   Si fallan se dibuja una parte del muñeco (cabeza, cuerpo ,brazos….).')
print('  Hay que conseguir adivinar la palabra antes que se complete el cuerpo.')
print('                       ¡O TERMINARAS AHORCADO!')
print('=' * 75)
print('\n\n')
print('=' * 75)
print('                        QUE COMIENCE EL JUEGO')
print('=' * 75)
print('\n\n')
print('=' * 75)
nombre = input('               Introduce tu nombre : ')
print('=' * 75)
print('\n\n')
print('=' * 75)
print("                 Hola",nombre, "comencemos con el juego")
print('=' * 75)
print('\n')


palabras = ("leon", "tigre")
palabra = random.choice(palabras)
letra_adivinadas=[]


while True:
    
    palabra_oculta = " "
    for c in palabra:
        if c in letra_adivinadas:
            palabra_oculta+=c
        else:
            palabra_oculta+= " _ "
    print(palabra_oculta)

    print('\n')
    text = input("Ingrese una letra del abecedario o la palabra completa: ").lower()
    print('\n')

    if text in palabra:
        letra_adivinadas.append(text)
        if set(letra_adivinadas)==set(palabra):
            print("Felicidades has Ganado la palabra es",(palabra))
            print('\n')
            break


