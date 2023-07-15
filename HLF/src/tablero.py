import numpy as np

import os, sys, random
sys.path.append(os.getcwd())
from HLF.utils import config

class Tablero:
    BOARD_SIZE = config.BOARD_SIZE
    EMPTY_SIGN = config.EMPTY_SIGN
    BOAT_SIGN = config.BOAT_SIGN
    BOAT_SIZES = config.BOAT_SIZES

    
    def __init__(self, size = None):
        if size is not None:
            self.BOARD_SIZE = size 
        
        bsize = (self.BOARD_SIZE, self.BOARD_SIZE)
        self.tablero = np.full(bsize, self.EMPTY_SIGN)

    def __clear_(self):
        '''
        Clear the board defore placing the boats
        '''
        self.tablero = np.full(shape=(self.BOARD_SIZE, self.BOARD_SIZE), fill_value=self.EMPTY_SIGN)

    def place_boat(self,coord_x, coord_y, orient, boat_size):
        tab = self.tablero.copy()

        if orient == "S":
            final_row = coord_x + boat_size
            tab[coord_x:final_row, coord_y] = self.BOAT_SIGN

        elif orient == "N":
            final_row = coord_x - boat_size + 1
            tab[final_row:(coord_x +1), coord_y] = self.BOAT_SIGN
        
        elif orient == "E":
            final_col = coord_y + boat_size
            tab[coord_x, coord_y:final_col] = self.BOAT_SIGN

        elif orient == "W":
            final_col = coord_y - boat_size + 1 # (2, 2) - (2, 0)
            tab[coord_x, final_col:(coord_y + 1)] = self.BOAT_SIGN

        return tab
    
    def initialize_boats(self):
        self.__clear_()
        for boat_size in self.BOAT_SIZES:
            while True:
                coord_x, coord_y = np.random.randint(0,self.BOARD_SIZE, size=2)
                orient = np.random.choice(["N","S","E","W"])
                cond_pos = self.valid_position(coord_x, coord_y, orient, boat_size)

                if cond_pos:
                    self.tablero = self.place_boat(coord_x, coord_y, orient, boat_size)

                    break

    def valid_position(self, coord_x, coord_y, orient, boat_size):
        tab = self.tablero.copy

        if orient == "S":
            final_row = coord_x + boat_size 
            cond_border = (final_row <= self.BOARD_SIZE)
            cond_over = np.any(tab[coord_x:final_row,coord_y] == \
                            self.BOAT_SIGN)
            
        if orient == "N":
            final_row = coord_x - boat_size + 1
            cond_border = (final_row >= 0)
            cond_over = np.any(tab[final_row:(coord_x + 1), coord_y] == \
                            self.BOAT_SIGN)

        elif orient == "E":
            final_col = coord_y + boat_size 
            cond_border = (final_col <=self.BOARD_SIZE)
            cond_over = np.any(tab[coord_x, coord_y:final_col] == \
                            self.BOAT_SIGN)
            
        elif orient == "W":
            final_col = coord_y - boat_size + 1
            cond_border = (final_col >= 0)
            cond_over = np.any(tab[coord_x, final_col:(coord_y + 1)] == \
                            self.BOAT_SIGN)
            
        return cond_border&(not cond_over)
    
if __name__ == "__main__":
    
    tablero_player = Tablero()
    print(tablero_player)