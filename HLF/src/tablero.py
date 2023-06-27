import numpy as np

import os, sys
sys.path.append(os.getcwd())
from HLF.utils import config

class Tablero:
    BOARD_SIZE = config.BOARD_SIZE
    EMPTY_SIGN = config.EMPTY_SIGN
    def __init__(self, size = None):
        if size is not None:
            self.BOARD_SIZE = size 
        
        bsize = (self.BOARD_SIZE, self.BOARD_SIZE)
        self.tablero = np.full((bsize, self.EMPTY_SIGN))

    def place_boat(self,coord_x, coord_y, orient, boat_size):
        tab = self.tablero.copy()
        if orient == "S":
            final_row = coord_x + boat_size
            tab[coord_x:final_row, coord_y] = self.BOAT_SIGN
        return tab

if __name__ == "__main__":
    
    tablero_player = Tablero()
    print(tablero_player)