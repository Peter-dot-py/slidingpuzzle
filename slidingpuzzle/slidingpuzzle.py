import random
import copy

# Create a blank space to represent the empty tile on the board

BLANK_SPACE = 0



def get_new_board(h: int, w: int):
    # Return a list of lists which represents a new board puzzle
    board = []
    counter = 1
    for _ in range(h):
        row = []
        for _ in range(w):  # _ means variable name doesn't matter
            row.append(counter)
            counter += 1
        board.append(row)
    board[-1][-1] = BLANK_SPACE
    return board



def find_blank_space(board) -> tuple[int, int]:  
    """
    Return a tuple containing the blank spaces coordinates

    Args:
        board: a list of list of ints representing a board

    Returns:
        A pair of ints repping the y, x coordinates of BLANKSPACE
     """
    
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] == BLANK_SPACE:
                return (y, x)  # y,x represtents row and col



  
def get_moves(board) -> list[tuple[int, int]]:
    moves = []
    empty_y, empty_x = find_blank_space(board)
    for y, x in (
        (empty_y-1, empty_x), 
        (empty_y, empty_x-1), 
        (empty_y+1, empty_x),
        (empty_y, empty_x+1)
    ):
        if 0 <= y < len(board) and 0 <= x < len(board[0]):
            moves.append((y, x))
    return moves      












def bfs(initial_board):
    height = len(initial_board)
    width = len(initial_board[0])
    goal = new_board(height, width)
    initial_history = []
    initial_state = (initial_board, initial_history)
    unvisited = [initial_state]
    visited_boards = []

    # begin BFS
    while len(unvisited) > 0:
        state = unvisited.pop()
        board, history = state

        # return move history when goal is found
        if goal == board:
            return history

        # check for duplicate
        if board in visited_boards:
            continue

        # make sure to record this so we don't repeat
        visited_boards.append(board)

        # construct next state
        moves = get_next_moves(board)
        for move in moves:
            next_board = copy.deepcopy(board)  # copy the current board
            apply_move(board, move)  # modify copied board
            next_history = history.copy()  # copy history
            next_history.append(move)  # record the new move to prior history
            next_state = (next_board, next_history)
            unvisited.insert(0, next_state)
