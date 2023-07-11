from HLF.src.player import Player
from HLF.src.tablero import Tablero
import numpy as np

tablero_jugador = Tablero()
tablero_maquina = Tablero()
jugador = Player()
maquina = Player()

print(jugador)
print(tablero_maquina)

# ====================== LAST UPDATE

def print_board(board):
    for row in board:
        print(" ".join(row))

def main():
    print("¡Bienvenido a Hundir la Flota!")
    print("Instrucciones:")
    print("- Introduce las coordenadas en el formato 'fila columna'. Por ejemplo, '2 3' para disparar en la fila 2, columna 3.")
    print("- Elige las coordenadas para hundir los barcos enemigos.")
    print("- ¡Buena suerte!\n")

    tablero_jugador = Tablero()
    tablero_maquina = Tablero()
    jugador = Player("Jugador")
    maquina = Player("Máquina")

    tablero_jugador.place_boat(0, 0, "S", 1)  # Ejemplo: Coloca un barco de 1 posición en el tablero del jugador

    # Comienza el juego
    while True:
        print("=== TURNO DEL JUGADOR ===")
        print("Tablero del jugador:")
        print_board(tablero_jugador.tablero)

        while True:
            disparo = input("Ingresa las coordenadas de tu disparo (fila columna): ").split()
            x, y = map(int, disparo)

            if 0 <= x < Tablero.BOARD_SIZE and 0 <= y < Tablero.BOARD_SIZE:
                break
            else:
                print("Coordenadas inválidas. Intenta nuevamente.")

        hit = jugador.shoot((x, y), tablero_maquina)
        if hit:
            print("¡Impacto!")
        else:
            print("Agua...")

        if tablero_maquina.tablero[x, y] == Tablero.HIT_SIGN:
            print("¡Hundiste un barco enemigo!")

        print("\n=== TURNO DE LA MÁQUINA ===")
        while True:
            disparo, hit = maquina.random_shot(tablero_jugador)
            x, y = disparo
            print(f"La máquina dispara en las coordenadas ({x}, {y}).")

            if hit:
                print("¡Impacto!")
            else:
                print("Agua...")

            if tablero_jugador.tablero[x, y] == Tablero.HIT_SIGN:
                print("¡La máquina hundió tu barco!")

            break  # Solo se realiza un disparo por turno de la máquina

        # Verificar si alguno de los jugadores se quedó sin barcos
        if np.count_nonzero(tablero_jugador.tablero == Tablero.BOAT_SIGN) == 0:
            print("\nLa máquina ganó. ¡Tus barcos han sido hundidos!")
            break

        if np.count_nonzero(tablero_maquina.tablero == Tablero.BOAT_SIGN) == 0:
            print("\n¡Felicidades! ¡Hundiste todos los barcos enemigos!")
            break

        print("=== SIGUIENTE TURNO ===\n")

if __name__ == "__main__":
    main()
