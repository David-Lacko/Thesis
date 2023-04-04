#min-max algorithm for game checkers

import numpy as np
import copy
from bot.config import *
from bot.can_moove import *
def min_max(board, player,figure, depth, move_mode = "deterministic"):
    if depth == 0:
        return eval_function(board, player), None
    elif can_moove(board, player) == []:
        return eval_function(board, player), None
    if player == figure:
        best_score = -100
        if move_mode == "deterministic":
            moves = need_move(board, player)
        else:
            moves = can_moove(board, player)
        # print(moves)
        for move in moves:
            temp_board = copy.deepcopy(board)
            temp_board = make_move(temp_board, move)
            if figure == "b":
                score = min_max(temp_board, "w", figure, depth - 1,move_mode)[0]
            else:
                score = min_max(temp_board, "b",figure, depth - 1,move_mode)[0]
            # print(score)
            if score > best_score:
                best_score = score
                best_move = move
        return best_score, best_move
    else:
        best_score = 100
        if move_mode == "deterministic":
            moves = need_move(board, player)
        else:
            moves = can_moove(board, player)
        for move in moves:
            temp_board = copy.deepcopy(board)
            temp_board = make_move(temp_board, move)
            if figure == "b":
                score = min_max(temp_board, "b", figure, depth - 1,move_mode)[0]
            else:
                score = min_max(temp_board, "w", figure, depth - 1,move_mode)[0]
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
        return -count
