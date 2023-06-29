import numpy as np

import os, sys
sys.path.append(os.getcwd())
from HLF.utils import config
from HLF.src.tablero import Tablero

def test_init_size():
    size = 5
    tablero_1 = Tablero()
    tablero_2 = Tablero(size)

    cond_1 = tablero_1.BOARD_SIZE == config.BOARD_SIZE
    cond_2 = tablero_2.BOARD_SIZE == size
    assert cond_1&cond_2

def test_tablero_init_values():
    tablero_1 = Tablero()
    cond_1 = tablero_1.tablero.shape[0] == config.BOARD_SIZE
    cond_2 = np.unique(tablero_1.tablero)[0] == config.EMPTY_SIGN
    assert cond_1&cond_2

def test_place_boat_size_2_board_5():
    size = 3
    boat_size = 2
    tablero_1 = Tablero(size)
    b = config.BOAT_SIGN
    e = config.EMPTY_SIGN

# ORIENTACION SUR
    coord_x, coord_y = (0,0)
    orient = "S"
    
    new_tab_S = tablero_1.place_boat(coord_x, coord_y, orient, boat_size)

    output_S = np.array([[b, e, e],
                        [b, e, e],
                        [e, e, e]])
    cond_S = np.all(output_S == new_tab_S)

# ORIENTACION NORTE   
    coord_x, coord_y = (2,0)
    orient = "N"
    
    new_tab_N = tablero_1.place_boat(coord_x, coord_y, orient, boat_size)

    output_N = np.array([[e, e, e],
                        [b, e, e],
                        [b, e, e]])
    cond_N = np.all(output_N == new_tab_N)

# ORIENTACION ESTE
    coord_x, coord_y = (0,0)
    orient = "E"
    
    new_tab_E = tablero_1.place_boat(coord_x, coord_y, orient, boat_size)

    output_E = np.array([[b, b, e],
                        [e, e, e],
                        [e, e, e]])
    cond_E = np.all(output_E == new_tab_E)

# ORIENTACION OESTE
    coord_x, coord_y = (0,2)
    orient = "W"
    
    new_tab_W = tablero_1.place_boat(coord_x, coord_y, orient, boat_size)

    output_W = np.array([[e, b, b],
                        [e, e, e],
                        [e, e, e]])
    cond_W = np.all(output_W == new_tab_W)

    assert np.all(cond_S & cond_N & cond_E & cond_W)