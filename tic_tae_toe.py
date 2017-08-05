import matplotlib.pyplot as plt
import random
import numpy as np


def create_board():
    """create a 3 by 3 board"""
    board = np.zeros((3,3))
    return board
board = create_board()



def place(board,player,position):
    """place"""
    if board[position] == 0:
        board[position] = player
        return board
place(board,1,(0,0))



def possibilities(board):
    for x in np.where(board):
        if x == 0:
            print(x)
            
possibilities(board)

def random_place(board, player):
    """randomly place a player"""
    possible_placements = possibilities(board)
    if len(possible_placements) > 0:
        possible_placements = random.choice(possible_placements)
        place(board, player, possible_placements)
    return board

random_place(board, 2)


board = create_board()
for i in range(3):
    for player in [1, 2]:
       random_place(board, player)
print(board)


def row_win(board,player):
    """check if a player wins in any row"""
    winner = False
    if np.any(np.all(board==player,axis=1)):
        return True
    else:
        return False

row_win(board, 1)

#7. player 2 column win
def col_win(board,player):
    """check if a player wins in any column"""
    winner = False
    if np.any(np.all(board==player,axis=0)):
        return True
    else:
        return False

col_win(board, 1)


def diag_win(board, player):
    """check if a player wins in any diagonal"""
    if np.all(np.diag(board)==player):
        return True
    else:
        return False
diag_win(board, 1)


def evaluate(board):
    winner = 0
    for player in [1, 2]:
        row_win(board, player)
        col_win(board, player)
        diag_win(board, player)
    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner

evaluate(board)


#Play the game
def play_game():
    board = create_board()
    winner = 0
    for i in range(9):
        for player in [1,2]:
            random_place(board, 1)
            evaluate(board)
            if winner == 1 or 2:
                return player
            else:
                print(-1)            
play_game()



import time
start = time.time()
games = [play_game() for i in range(1000)]
end = time.time()
# print(games)
print (end-start)

plt.hist(games)
plt.show()



def play_strategic_game():
    board, winner = create_board(), 0
    board[1,1] = 1
    while winner == 0:
        for player in [2,1]:
            # use `random_place` to play a game, and store as `board`.
            random_place(board,player)
            winner = evaluate(board)
            # use `evaluate(board)`, and store as `winner`.
            if winner != 0:
                break
    return winner

play_strategic_game()



import time
start = time.time()
games = [play_strategic_game() for i in range(1000)]
end = time.time()
# print(games)
print (end-start)

plt.hist(games)
plt.show()










