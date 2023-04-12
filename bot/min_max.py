#min-max algorithm for game checkers

import numpy as np
import copy
from bot.config import *
from bot.can_moove import *
def min_max(board, player,maximizer, depth, move_mode = "deterministic"):
    if depth == 0:
        return eval_function(board, player), None
    elif can_moove(board, player) == []:
        return eval_function(board, player), None
    if maximizer:
        best_score = -100
        if move_mode == "deterministic":
            moves = need_move(board, player)
        else:
            moves = can_moove(board, player)
        best = []
        for move in moves:
            temp_board = copy.deepcopy(board)
            temp_board = make_move(temp_board, move)
            if player == "b":
                score = min_max(temp_board, "w", False, depth - 1,move_mode)[0]
            else:
                score = min_max(temp_board, "b",False, depth - 1,move_mode)[0]
            if score > best_score:
                best_score = score
                best = [move]
            elif score == best_score:
                best.append(move)
        if best_score == 0:
            return 0,random.choice(moves)

        return best_score, random.choice(best)
    else:
        best_score = 100
        if move_mode == "deterministic":
            moves = need_move(board, player)
        else:
            moves = can_moove(board, player)
        best = []
        for move in moves:
            temp_board = copy.deepcopy(board)
            temp_board = make_move(temp_board, move)
            if player == "b":
                score = min_max(temp_board, "w", True, depth - 1,move_mode)[0]
            else:
                score = min_max(temp_board, "b", True, depth - 1,move_mode)[0]
            # print(score)
            if score < best_score:
                best_score = score
                best = [move]
            elif score == best_score:
                best.append(move)
        if best_score == 0:
            return 0,random.choice(moves)
        return best_score, random.choice(best)


