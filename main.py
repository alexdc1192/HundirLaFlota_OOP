from HLF.src.player import Player
from HLF.src.tablero import Tablero
from HLF.utils.config import COMP_NAME

import numpy as np
import time

# Definición de la lógica del juego 

tablero_jugador = Tablero()
tablero_maquina = Tablero()
tablero_maquina_pub = Tablero()

name = input("Introduce tu nombre: ")
jugador = Player(name)
maquina = Player(COMP_NAME)

# Añadimos/Inicializamos los barcos
tablero_jugador.initialize_boats()
tablero_maquina.initialize_boats()

print(tablero_jugador.tablero)
print("\n")
print(tablero_maquina_pub.tablero)
print("\n")

while True:
    print(f"\nTURNO DE{jugador.name.upper()}")
    x = int(input('Introduzca coordenada X: \n'))
    y = int(input('Introduzca coordenada Y: \n'))
    print(f"DISPARA EN ({x}, {y})\n")
    tablero_maquina.tablero = jugador.shoot(x, y, tablero_maquina)
    tablero_maquina_pub.tablero[x, y] = tablero_maquina.tablero[x, y]

    print(tablero_jugador.tablero)
    print("\n")
    print(tablero_maquina.tablero)
    print("\n\n")

    if not np.any(tablero_maquina.tablero == tablero_maquina.BOAT_SIGN):
        print(f"\n{jugador.name.upper()} GANA!!!\n")
        break
    time.sleep (2)

    while True:
        try:
            x_maq, y_maq = np.random.randint(0, tablero_jugador.BOARD_SIZE, size=2)
            tablero_jugador.tablero = maquina.shoot(x_maq, y_maq,tablero_jugador)
            break
        except ValueError:
            continue

    print(f"\nTURNO DE {maquina.name.upper()}")
    print(f"DISPARA EN ({x_maq}, {y_maq})\n")

    print(tablero_jugador.tablero)
    print("\n")
    print(tablero_maquina_pub.tablero)
    print("\n\n")
    
    if not np.any(tablero_jugador.tablero == tablero_jugador.BOAT_SIGN):
        print(f"\n{maquina.name.upper()} GANA!!!\n")