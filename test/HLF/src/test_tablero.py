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
    coord_x, coord_y = (0,0)
    orient = "S"
    boat_size = 2

    tablero_1 = Tablero(size)
    new_tab = tablero_1.place_boat(coord_x, coord_y, orient, boat_size)
    b = config.BOAT_SIGN
    e = config.EMPTY_SIGN
    exp_out = np.array([[b, e, e],
                        [b, e, e],
                        [e, e, e]])

    assert np.all(new_tab == exp_out)