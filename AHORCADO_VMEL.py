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
print('=' * 75)
abecedario = print('                                 ABECEDARIO')
print('\n')
print ('A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z')
print('=' * 75)

def inicio():
    print("   ▄████████    ▄█    █▄     ▄██████▄     ▄████████  ▄████████    ▄████████ ████████▄   ▄██████▄")
    print("  ███    ███   ███    ███   ███    ███   ███    ███ ███    ███   ███    ███ ███   ▀███ ███    ███")
    print("  ███    ███   ███    ███   ███    ███   ███    ███ ███    █▀    ███    ███ ███    ███ ███    ███")
    print("  ███    ███  ▄███▄▄▄▄███▄▄ ███    ███  ▄███▄▄▄▄██▀ ███          ███    ███ ███    ███ ███    ███")
    print("▀███████████ ▀▀███▀▀▀▀███▀  ███    ███ ▀▀███████▀   ███        ▀███████████ ███    ███ ███    ███")
    print("  ███    ███   ███    ███   ███    ███ ▀███████████ ███    █▄    ███    ███ ███    ███ ███    ███")
    print("  ███    ███   ███    ███   ███    ███   ███    ███ ███    ███   ███    ███ ███   ▄███ ███    ███")
    print("  ███    █▀    ███    █▀     ▀██████▀    ███    ███ ████████▀    ███    █▀  ████████▀   ▀██████▀")


def congratulation():
    print("███████╗███████╗██╗     ██╗ ██████╗██╗██████╗  █████╗ ██████╗ ███████╗███████╗")
    print("██╔════╝██╔════╝██║     ██║██╔════╝██║██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝")
    print("█████╗  █████╗  ██║     ██║██║     ██║██║  ██║███████║██║  ██║█████╗  ███████╗")
    print("██╔══╝  ██╔══╝  ██║     ██║██║     ██║██║  ██║██╔══██║██║  ██║██╔══╝  ╚════██║")
    print("██║     ███████╗███████╗██║╚██████╗██║██████╔╝██║  ██║██████╔╝███████╗███████║")
    print("╚═╝     ╚══════╝╚══════╝╚═╝ ╚═════╝╚═╝╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚══════╝")




print('\n')
inicio()
print('\n')

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

def mostrar_escenario(errores):
    escena = escenario
    for i in range(0, len (simbolos)):
        simbolo = simbolos [i]
        escena = escena.replace(str(i), simbolo)
    print(escena)

palabras = ("leon", "tigre")
palabra = random.choice(palabras)
letra_adivinadas=[]
lista_abecedario = list('abcdefghijklmnñopqrstuvwxyz')
intentos = 6


print(f'Tienes {intentos} intentos antes de perden BUENA SUERTE!')
print(simbolos[6 - intentos])
print('\n')

while intentos>0:

    palabra_oculta = " "
    for c in palabra:
        if c in letra_adivinadas:
            palabra_oculta+=c
            intentos>1
        else:
            palabra_oculta+= "_"
    print(palabra_oculta)

    print('\n')
    text = input("Ingrese una letra del abecedario o la palabra completa: ").lower()
    print('\n')
    
    if text in letra_adivinadas:
        print("Ya has introducido esa letra. Prueba con otra.")
        continue

    if text in palabra:
        letra_adivinadas.append(text)
        if set(letra_adivinadas)==set(palabra):
            congratulation()
            print('\n')
            print("Felicidades has Ganado la palabra es",(palabra))
            break
    else:
        intentos-=1
        print('\n')
        print(f"Letra incorrecta, Te qudan",(intentos),"oportunidades")
        print('\n')

    if intentos==0:
        print(f"Lo sineto has perdido, la palabra era",(palabra))

    elif len(text) == len(palabra):
        if text == palabra:
            congratulation()
            print('\n')
            print("Has ganado la palabra completa es",(palabra))
            print('\n')
            break
print('\n')
