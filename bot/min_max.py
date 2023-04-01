#min-max algorithm for game checkers

import numpy as np
import copy
from bot.config import *
from bot.can_moove import *
def min_max(board, player, depth):
    if depth == 0:
        return eval_function(board, player), None
    elif can_moove(board, player) == []:
        return eval_function(board, player), None
    if player == "b":
        best_score = -100
        moves = need_move(board, player)
        # print(moves)
        for move in moves:
            temp_board = copy.deepcopy(board)
            temp_board = make_moves(temp_board, move,moves)
            score = min_max(temp_board, "w", depth - 1)[0]
            # print(score)
            if score > best_score:
                best_score = score
                best_move = move
        return best_score, best_move
    else:
        best_score = 100
        moves = need_move(board, player)
        for move in moves:
            temp_board = copy.deepcopy(board)
            temp_board = make_moves(temp_board, move,moves)
            score = min_max(temp_board, "b", depth - 1)[0]
            # print(score)
            if score < best_score:
                best_score = score
                best_move = move
        return best_score, best_move

def eval_function(board, player):
    count = 0
    for i in range(8):
        for j in range(8):
            if board[i][j] == 1:
                count += 1
            elif board[i][j] == 3:
                count += 2
            elif board[i][j] == 2:
                count -= 1
            elif board[i][j] == 4:
                count -= 2
    if player == "b":
        return count
    else:
        # print(board)
        return -count
