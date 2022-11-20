from slidingpuzzle import *


def test_create_board():
    board = get_new_board(3, 3)
    truth = [[1, 2, 3], [4, 5, 6], [7, 8, BLANK_SPACE]]
    assert board == truth  # assert raises exception if thing on right is not true
    

def test_find_blank_space():
    board = get_new_board(3, 3)
    pos = find_blank_space(board)
    assert pos == (2, 2)
    assert board[pos[0]][pos[1]] == BLANK_SPACE 
     
def test_get_moves():
    moves = get_moves(get_new_board)
    assert len(moves) == 2