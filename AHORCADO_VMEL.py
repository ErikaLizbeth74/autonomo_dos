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
print("                 Hola",nombre, "comencemos con el juego")
print('\n')

import random

escenario = \
    '''   
~~~~~~~~~~~
+-----+
|     0
|     1
|   4 23
|    5   
|            
~~~~~~~~~~~   
'''

simbolos = '|💀🦺🫱🫲🦴'

escena = escenario
for i in range(0, len(simbolos)):
    simbolo = simbolos[i]
    escena = escena.replace(str(i), simbolo)
print(escena)

## PARTE  DOS DEL TRABAJO
## PARTE  DOS DEL TRABAJO
## PARTE  DOS DEL TRABAJO
## PARTE  DOS DEL TRABAJO
## PARTE  DOS DEL TRABAJO

palabras = ("leon", "tigre", "delfin", "manzana", "perro", "mandarina", "sandia")
palabra = random.choice(palabras)
letra_adivinadas=[]

while True:

    text = input("Ingrese una letra del abecedario o la palabra completa: ").lower()
    letra_adivinadas.append(text)
    
    palabra_oculta = " "
    for c in palabra:
        if c in letra_adivinadas:
            palabra_oculta+=c
        else:
            palabra_oculta+= "_"
    print(palabra_oculta)

    if "_" not in palabra_oculta:
        print("Felicidades has Ganado la palabra es",(palabra))
        break

    elif len(text) == len(palabra):
        if text == palabra:
            print("Has ganado la palabra es",(palabra))
            break
    



print('\n\n')
