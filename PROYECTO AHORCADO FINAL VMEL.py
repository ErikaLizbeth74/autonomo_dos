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
print('                              ABECEDARIO')
print('\n')
print ('A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z')
print('=' * 75)

def inicio():
    print("    ▄█████▄ ██   ██  ▄████▄  ██████▄  ▄██████ ▄█████▄ ██████▄   ▄████▄ ")
    print("    ██   ██ ██   ██ ██    ██ ██    ██ ██   ██ ██   ██ ██   ▀██ ██    ██")
    print("    ███████ ██▀▀▀██ ██    ██ ██████▀  ██      ███████ ██    ██ ██    ██")
    print("    ██   ██ ██   ██ ██    ██ ██   ██  ██   ██ ██   ██ ██   ▄██ ██    ██")
    print("    ██   ██ ██   ██  ▀████▀  ██    ██ ▀█████▀ ██   ██ ██████▀   ▀████▀ ")

def Perdida():
    print("  ▄█████▄ ▄█████▄ ██████▄  ██████▄ ██ ▄█████▄ ▄██████▄ ██████▄")
    print("  ██   ██ ██      ██    ██ ██  ▀██ ██ ██         ██    ██     ")
    print("  ██████▀ █████   ██████▀  ██   ██ ██ ▀█████▄    ██    █████  ")
    print("  ██      ██      ██   ██  ██  ▄██ ██      ██    ██    ██     ")
    print("  ██      ██████▀ ██    ██ █████▀  ██ ▀█████▀    ██    ██████▀")

def Felicidades():
    print("▄█████▄ ▄█████▄ ██      ██  ▄████▄ ██ █████▄   ▄███▄  █████▄  ▄█████▄ ▄█████▄")
    print("██      ██      ██      ██ ██   ██ ██ ██   ██ ██   ██ ██   ██ ██      ██     ")
    print("█████   █████   ██      ██ ██      ██ ██   ██ ███████ ██   ██ █████   ▀█████▄")
    print("██      ██      ██      ██ ██   ██ ██ ██   ██ ██   ██ ██   ██ ██           ██")
    print("██      ▀█████▀ ▀█████▀ ██  ▀████▀ ██ █████▀  ██   ██ █████▀  ▀█████▀ ▀█████▀")
   
print('\n')
inicio()
print('\n')

def mostrar_tablero(intentos):
    figura = [
        '''
          +---+
          |   |
          O   |
         /|\\  |
         / \\  |
              |
        ========''',
        '''
          +---+
          |   |
          O   |
         /|\\  |
         /    |
              |
        ========''',
        '''
          +---+
          |   |
          O   |
         /|\\  |
              |
              |
        ========''',
        '''
          +---+
          |   |
          O   |
         /|   |
              |
              |
        ========''',
        '''
          +---+
          |   |
          O   |
          |   |
              |
              |
        ========''',
         '''
          +---+
          |   |
          O   |
              |
              |
              |
        ========''',
        '''
          +---+
          |   |
              |
              |
              |
              |
        ========'''
    ]
    print(figura[intentos])

def jugar ():

    palabras = ("leon", "tigre","manzana","perro","geopardo","mandarina","coco","vinocunga")
    palabra = random.choice(palabras)
    letra_adivinadas=[]
    intentos = 6
    
    print('\n')
    print(f'Tienes {intentos} intentos antes de perden BUENA SUERTE!')
    print('\n')

    while True:

        mostrar_tablero(intentos)
        print('\n')

        palabra_oculta = " "
        for c in palabra:
            if c in letra_adivinadas:
                palabra_oculta+=c
                intentos>1
            else:
                palabra_oculta+= " _ "
        print(palabra_oculta)

        print('\n')
        text = input("Ingrese una letra del abecedario o la palabra completa: ").lower()
        print('\n')
        valida = 'a' <= text <= 'z'
        if not valida:
                print('Error solo se permite letras no numneros')
                continue
        print('\n')
        
        if text in letra_adivinadas:
            print('Ya has introducido la letra',text,'Prueba con otra.')
            continue

        if text in palabra:
            letra_adivinadas.append(text)
            if set(letra_adivinadas)==set(palabra):
                print("Felicidades has Ganado la palabra es",(palabra))
                print('\n')
                Felicidades()
                break
        else:
            intentos-=1
            print('\n')
            print(f"Letra o palabra incorrecta, Te qudan",(intentos),"oportunidades")
            print('\n')

        if intentos==0:
            print('\n')
            print(f"Lo sineto has perdido, la palabra era",(palabra))
            print('\n')
            Perdida()
            break

        elif set(text) == set(palabra):
            if text == palabra:
                print("Has ganado la palabra completa es",(palabra))
                print('\n')
                Felicidades()
            break

    print('\n')
    jugar_otra_vez = input("¿Quieres jugar de nuevo? (si/no): ").lower()
    if jugar_otra_vez == "si":
        jugar()
        print('\n')
    else:
        print("¡Gracias por jugar!")
    print('\n')

jugar()

