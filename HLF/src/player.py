import numpy as np

import os, sys
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
# (borrador, a revisar) ========= LAST UPDATE
    def shoot(self, coordinates, board):
        x, y = coordinates
        cell = board.get_cell(x, y)  # Obtener la celda del tablero en las coordenadas dadas

        if cell == Tablero.BOAT_SIGN:  # Si la celda contiene un barco
            board.mark_ship_hit(x, y)  # Marcar el barco como impactado en el tablero
            return True  # Retorna True para indicar que hubo un impacto
        else:
            board.mark_shot(x, y, False)
            return False  # Retorna False para indicar que fue un disparo fallido
        