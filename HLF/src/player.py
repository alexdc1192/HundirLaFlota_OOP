import numpy as np

import os, sys, random
sys.path.append(os.getcwd())
from HLF.utils import config
from HLF.src.tablero import Tablero


class Player:

# CONSTANTES

    WATER_SIGN = config.WATER_SIGN
    HIT_SIGN = config.HIT_SIGN

# ACCIONES Y METODOS

# Nombre del jugador
    def __init__(self, name):
        self.name = name
        
# Método para disparar, pidiendo coordenadas del disparo y tablero donde se dispara
    def shoot(self, coordinates, board):
        x, y = coordinates
        cell = board.get_cell(x, y)  # Obtener la celda del tablero en las coordenadas dadas

        if cell == Tablero.BOAT_SIGN:  # Si la celda contiene un barco
            board.mark_ship_hit(x, y)  # Marcar el barco como impactado en el tablero
            return True  # Retorna True para indicar que hubo un impacto
        else:
            board.mark_shot(x, y, False)
            return False  # Retorna False para indicar que fue un disparo fallido
        
# ====================== LAST UPDATE

    def random_shot(self, board):
        while True:
            x = random.randint(0, Tablero.BOARD_SIZE - 1)
            y = random.randint(0, Tablero.BOARD_SIZE - 1)
            cell = board.get_cell(x, y)

            if cell == Tablero.EMPTY_SIGN:
                break

        hit = self.shoot((x, y), board)
        return (x, y), hit

    def __str__(self):
        return f"Player: {self.name}"

# ====================== LAST UPDATE
if __name__ == "__main__":
        
    alex_player = Player("Alex")
    maquina_tablero = Tablero()
    print(alex_player)       