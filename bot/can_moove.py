import random

import numpy as np
import copy

def can_moove(board, figure):
    moves = []
    for x in range(8):
        for y in range(8):
            if figure == "w" and board[x][y] == 1:
                move = can_remuve_white(board, x, y)
                if "left2" in move:
                    moves.append([x, y, x + 2, y - 2])
                    for mov in next_move(copy.deepcopy(board),[x, y, x + 2, y - 2]):
                        moves.append(mov)
                if "right2" in move:
                    moves.append([x, y, x + 2, y + 2])
                    for mov in next_move(copy.deepcopy(board),[x, y, x + 2, y + 2]):
                        moves.append(mov)
                if "left" in move:
                    moves.append([x, y, x + 1, y - 1])
                if "right" in move:
                    moves.append([x, y, x + 1, y + 1])

            elif figure == "b" and board[x][y] == 2:
                move = can_remuve_black(board, x, y)
                if "left2" in move:
                    moves.append([x, y, x - 2, y - 2])
                    for mov in next_move(copy.deepcopy(board),[x, y, x - 2, y - 2]):
                        moves.append(mov)
                if "right2" in move:
                    moves.append([x, y, x - 2, y + 2])
                    for mov in next_move(copy.deepcopy(board),[x, y, x - 2, y + 2]):
                        moves.append(mov)
                if "left" in move:
                    moves.append([x, y, x - 1, y - 1])
                if "right" in move:
                    moves.append([x, y, x - 1, y + 1])

            elif figure == "w" and board[x][y] == 3:
                r_move = can_remuve_queen(board, x, y,[1,3],[2,4])
                move = can_moove_queen(board, x, y)
                for i in r_move:
                    moves.append(i)
                    for mov in next_move(copy.deepcopy(board),i):
                        moves.append(mov)
                for i in move:
                    moves.append(i)
            elif figure == "b" and board[x][y] == 4:
                r_move = can_remuve_queen(board, x, y,[2,4],[1,3])
                move = can_moove_queen(board, x, y)
                for i in r_move:
                    moves.append(i)
                    for mov in next_move(copy.deepcopy(board),i):
                        moves.append(mov)
                for i in move:
                    moves.append(i)
    return moves

def can_remuve_white(board, x, y, figure):
    moves = []
    if figure == "w" and board[x][y] == 1:
        move = can_remuve_white(board, x, y)
        if "left2" in move:
            moves.append([x, y, x + 2, y - 2])
            for mov in next_move(copy.deepcopy(board), [x, y, x + 2, y - 2]):
                moves.append(mov)
        if "right2" in move:
            moves.append([x, y, x + 2, y + 2])
            for mov in next_move(copy.deepcopy(board), [x, y, x + 2, y + 2]):
                moves.append(mov)
        if "left" in move:
            moves.append([x, y, x + 1, y - 1])
        if "right" in move:
            moves.append([x, y, x + 1, y + 1])

    elif figure == "b" and board[x][y] == 2:
        move = can_remuve_black(board, x, y)
        if "left2" in move:
            moves.append([x, y, x - 2, y - 2])
            for mov in next_move(copy.deepcopy(board), [x, y, x - 2, y - 2]):
                moves.append(mov)
        if "right2" in move:
            moves.append([x, y, x - 2, y + 2])
            for mov in next_move(copy.deepcopy(board), [x, y, x - 2, y + 2]):
                moves.append(mov)
        if "left" in move:
            moves.append([x, y, x - 1, y - 1])
        if "right" in move:
            moves.append([x, y, x - 1, y + 1])

    elif figure == "w" and board[x][y] == 3:
        r_move = can_remuve_queen(board, x, y, [1, 3], [2, 4])
        move = can_moove_queen(board, x, y)
        for i in r_move:
            moves.append(i)
            for mov in next_move(copy.deepcopy(board), i):
                moves.append(mov)
        for i in move:
            moves.append(i)
    elif figure == "b" and board[x][y] == 4:
        r_move = can_remuve_queen(board, x, y, [2, 4], [1, 3])
        move = can_moove_queen(board, x, y)
        for i in r_move:
            moves.append(i)
            for mov in next_move(copy.deepcopy(board), i):
                moves.append(mov)
        for i in move:
            moves.append(i)
    return moves


def need_move(board, figure):
    moves = []
    for x in range(8):
        for y in range(8):
            if figure == "w" and board[x][y] == 1:
                move = can_remuve_white(board, x, y)
                if "left2" in move:
                    moves.append([x, y, x + 2, y - 2])
                    for mov in next_move(copy.deepcopy(board),[x, y, x + 2, y - 2]):
                        moves.append(mov)
                if "right2" in move:
                    moves.append([x, y, x + 2, y + 2])
                    for mov in next_move(copy.deepcopy(board),[x, y, x + 2, y + 2]):
                        moves.append(mov)
            elif figure == "b" and board[x][y] == 2:
                move = can_remuve_black(board, x, y)
                if "left2" in move:
                    moves.append([x, y, x - 2, y - 2])
                    for mov in next_move(copy.deepcopy(board),[x, y, x - 2, y - 2]):
                        moves.append(mov)
                if "right2" in move:
                    moves.append([x, y, x - 2, y + 2])
                    for mov in next_move(copy.deepcopy(board),[x, y, x - 2, y + 2]):
                        moves.append(mov)
            elif figure == "w" and board[x][y] == 3:
                r_move = can_remuve_queen(board, x, y,[1,3],[2,4])
                for i in r_move:
                    moves.append(i)
                    for mov in next_move(copy.deepcopy(board),i):
                        moves.append(mov)
            elif figure == "b" and board[x][y] == 4:
                r_move = can_remuve_queen(board, x, y,[2,4],[1,3])
                for i in r_move:
                    moves.append(i)
                    for mov in next_move(copy.deepcopy(board),i):
                        moves.append(mov)
    if moves == []:
        return can_moove(board, figure)
    return moves

def can_remuve_white(board, x, y):
    if y < 6 and y > 1 and x < 6:
        if board[x + 2][y - 2] == 0 and board[x + 2][y + 2] == 0 and \
                (board[x + 1][y - 1] == 2 or board[x + 1][y - 1] == 4) and \
                (board[x + 1][y + 1] == 2 or board[x + 1][y + 1] == 4):
            return ["left2", "right2"]
        if board[x + 2][y - 2] == 0 and (board[x + 1][y - 1] == 2 or board[x + 1][y - 1] == 4):
            val = can_moove_white(board, x, y)
            if val:
                return ["left2",val[0]]
            return ["left2"]
        if board[x + 2][y + 2] == 0 and (board[x + 1][y + 1] == 2 or board[x + 1][y + 1] == 4):
            val = can_moove_white(board, x, y)
            if val:
                return ["right2",val[0]]
            return ["right2"]
    elif (y == 7 or y ==6) and x < 6:
        if board[x + 2][y - 2] == 0 and (board[x + 1][y - 1] == 2 or board[x + 1][y - 1] == 4):
            add = can_moove_white(board, x, y)
            if add:
                return ["left2",add[0]]
            return ["left2"]
    elif (y == 0 or y == 1) and x < 6:
        if board[x + 2][y + 2] == 0 and (board[x + 1][y + 1] == 2 or board[x + 1][y + 1] == 4):
            add = can_moove_white(board, x, y)
            if add:
                return ["right2",add[0]]
            return ["right2"]
    return can_moove_white(board, x, y)

def can_moove_white(board, x, y):
    if x < 7 and y < 7 and y > 0:
        if board[x + 1][y - 1] == 0 and board[x + 1][y + 1] == 0:
            return ["left", "right"]
        elif board[x + 1][y - 1] == 0:
            return ["left"]
        elif board[x + 1][y + 1] == 0:
            return ["right"]
    elif y == 7 and x < 7:
        if board[x + 1][y - 1] == 0:
            return ["left"]
    elif y == 0 and x < 7:
        if board[x + 1][y + 1] == 0:
            return ["right"]
    return []

def can_remuve_black(board, x, y):
    if y < 6 and y > 1 and x > 1:
        if board[x - 2][y - 2] == 0 and board[x - 2][y + 2] == 0 and \
                (board[x - 1][y - 1] == 1 or board[x - 1][y - 1] == 3) and \
                (board[x - 1][y + 1] == 1 or board[x - 1][y + 1] == 3):

            return ["left2", "right2"]
        if board[x - 2][y - 2] == 0 and (board[x - 1][y - 1] == 1 or board[x - 1][y - 1] == 3):
            return ["left2", can_moove_black(board, x, y)[0]]
        if board[x - 2][y + 2] == 0 and (board[x - 1][y + 1] == 1 or board[x - 1][y + 1] == 3):
            return ["right2",can_moove_black(board, x, y)[0]]
    elif (y == 7 or y ==6) and x > 1:
        if board[x - 2][y - 2] == 0 and (board[x - 1][y - 1] == 1 or board[x - 1][y - 1] == 3):
            return ["left2",can_moove_black(board, x, y)[0]]
    elif (y == 0 or y == 1) and x > 1:
        if board[x - 2][y + 2] == 0 and (board[x - 1][y + 1] == 1 or board[x - 1][y + 1] == 3):
            return ["right2",can_moove_black(board, x, y)[0]]
    return can_moove_black(board, x, y)

def can_moove_black(board, x, y):
    if x > 0 and y < 7 and y > 0:
        if board[x - 1][y - 1] == 0 and board[x - 1][y + 1] == 0:
            return ['left', 'right']
        elif board[x - 1][y - 1] == 0:
            return ['left']
        elif board[x - 1][y + 1] == 0:
            return ['right']
    elif y == 7 and x > 0:
        if board[x - 1][y - 1] == 0:
            return ['left']
    elif y == 0 and x > 0:
        if board[x - 1][y + 1] == 0:
            return ['right']
    return ['none']

def can_moove_queen(board, x, y):
    top = 7 - x
    bottom = x
    left = y
    right = 7 - y
    top_left = min(top, left)
    top_right = min(top, right)
    bottom_left = min(bottom, left)
    bottom_right = min(bottom, right)
    max_move = []
    for i in range(1, top_left + 1):
        if board[x + i][y - i] == 0:
            max_move.append([x, y, x + i, y - i])
        else:
            break
    for i in range(1, top_right + 1):
        if board[x + i][y + i] == 0:
            max_move.append([x, y, x + i, y + i])
        else:
            break
    for i in range(1, bottom_left + 1):
        if board[x - i][y - i] == 0:
            max_move.append([x, y, x - i, y - i])
        else:
            break
    for i in range(1, bottom_right + 1):
        if board[x - i][y + i] == 0:
            max_move.append([x, y, x - i, y + i])
        else:
            break
    return max_move

def can_remuve_queen(board, x, y,onw,enemy):
    top = 7 - x
    bottom = x
    left = y
    right = 7 - y
    top_left = min(top, left)
    top_right = min(top, right)
    bottom_left = min(bottom, left)
    bottom_right = min(bottom, right)
    max_move = []
    if top_left > 1:
        for i in range(1, top_left):
            if board[x + i][y - i] == onw[0] or board[x + i][y - i] == onw[1]:
                break
            elif board[x + i][y - i] == enemy[0] or board[x + i][y - i] == enemy[1]:
                if board[x + i + 1][y - i - 1] == 0:
                    max_move.append([x, y, x + i + 1, y - i - 1])
                break
    if top_right > 1:
        for i in range(1, top_right):
            if board[x + i][y + i] == onw[0] or board[x + i][y + i] == onw[1]:
                break
            elif board[x + i][y + i] == enemy[0] or board[x + i][y + i] == enemy[1]:
                if board[x + i + 1][y + i + 1] == 0:
                    max_move.append([x, y, x + i + 1, y + i + 1])
                break
    if bottom_left > 1:
        for i in range(1, bottom_left):
            if board[x - i][y - i] == onw[0] or board[x - i][y - i] == onw[1]:
                break
            elif board[x - i][y - i] == enemy[0] or board[x - i][y - i] == enemy[1]:
                if board[x - i - 1][y - i - 1] == 0:
                    max_move.append([x, y, x - i - 1, y - i - 1])
                break
    if bottom_right > 1:
        for i in range(1, bottom_right):
            if board[x - i][y + i] == onw[0] or board[x - i][y + i] == onw[1]:
                break
            elif board[x - i][y + i] == enemy[0] or board[x - i][y + i] == enemy[1]:
                if board[x - i - 1][y + i + 1] == 0:
                    max_move.append([x, y, x - i - 1, y + i + 1])
                break
    return max_move

def select_random_move(moves):
    if len(moves) > 0:
        return random.choice(moves)
    return 0

def make_moves(bord, move, all_moves):
    if bord[move[0]][move[1]] != 0:
        return make_move(bord, move)
    else:
        print(move)
        print(all_moves)
        print(bord)
        need_move = [move]
        all_moves.remove(move)
        moved = []
        # finde end position
        for moves in all_moves:
            if move[0] == moves[2] and move[1] == moves[3] and move[2] == moves[0] and move[3] == moves[1]:
                all_moves.remove(moves)

        while bord[move[0]][move[1]] == 0:
            for moves in all_moves:
                if move[0] == moves[2] and move[1] == moves[3]:
                    need_move.append(moves)
                    all_moves.remove(moves)
                    moved.append([move[0], move[1]])
                    move = moves
        for move in reversed(need_move):
            bord = make_move(bord, move)


        return bord




def make_move(board, move):
    x1 = int(move[0])
    y1 = int(move[1])
    x2 = int(move[2])
    y2 = int(move[3])
    board[x2][y2] = board[x1][y1]
    board[x1][y1] = 0
    board = remuve_skiped(board, x1, y1, x2, y2)
    return board

def next_moves(bord,x,y):
    moves = []
    if bord[x][y] == 1:
        move = can_remuve_white(bord,x,y)
        if "left2" in move:
            moves.append([x, y, x + 2, y - 2])
        if "right2" in move:
            moves.append([x, y, x + 2, y + 2])
    elif bord[x][y] == 2:
        move = can_remuve_black(bord,x,y)
        if "left2" in move:
            moves.append([x, y, x - 2, y - 2])
        if "right2" in move:
            moves.append([x, y, x - 2, y + 2])
    elif bord[x][y] == 3:
        move = can_remuve_queen(bord,x,y,[3,1],[2,4])

        for i in move:
            moves.append([x, y, i[2], i[3]])
    elif bord[x][y] == 4:
        move = can_remuve_queen(bord,x,y,[2,4],[1,3])
        for i in move:
            moves.append([x, y, i[2], i[3]])
    return moves


def next_move(bord,move):
    bord = make_move(bord,move)
    moves = []
    x2,y2 = move[2],move[3]
    new_moves = next_moves(bord,x2,y2)
    while len(new_moves) > 0:
        for move in new_moves:
            moves.append(move)
            bord = make_move(bord, move)
            x2, y2 = move[2], move[3]
            new_moves = next_moves(bord, x2, y2)
    return moves






def remuve_skiped(board, x1, y1, x2, y2):
    # all positions between x1,y1 and x2,y2
    move = abs(x2 - x1)
    for i in range(1, move):
        if x1 < x2 and y1 < y2:
            board[x1 + i][y1 + i] = 0
        elif x1 < x2 and y1 > y2:
            board[x1 + i][y1 - i] = 0
        elif x1 > x2 and y1 < y2:
            board[x1 - i][y1 + i] = 0
        elif x1 > x2 and y1 > y2:
            board[x1 - i][y1 - i] = 0
    return board

def change_to_queen(board):
    for i in range(8):
        if board[7][i] == 1:
            board[7][i] = 3
        if board[0][i] == 2:
            board[0][i] = 4
    return board

def run(board,figure):
    moves = need_move(board, figure)
    # move = select_random_move(moves)
    # if move != 0:
    #     moves = can_moove(board, figure)
    move = select_random_move(moves)
    if move != 0:
        board = make_moves(board, move, moves)
    else:
        return False, False
    board = change_to_queen(board)
    return board, move

def can_moove_figure(board,x,y, figure):
    moves = []
    if figure == "w" and board[x][y] == 1:
        move = can_remuve_white(board, x, y)
        if "left2" in move:
            moves.append([x, y, x + 2, y - 2])
            for mov in next_move(copy.deepcopy(board),[x, y, x + 2, y - 2]):
                moves.append(mov)
        if "right2" in move:
            moves.append([x, y, x + 2, y + 2])
            for mov in next_move(copy.deepcopy(board),[x, y, x + 2, y + 2]):
                moves.append(mov)
        if "left" in move:
            moves.append([x, y, x + 1, y - 1])
        if "right" in move:
            moves.append([x, y, x + 1, y + 1])
    elif figure == "b" and board[x][y] == 2:
        move = can_remuve_black(board, x, y)
        if "left2" in move:
            moves.append([x, y, x - 2, y - 2])
            for mov in next_move(copy.deepcopy(board),[x, y, x - 2, y - 2]):
                moves.append(mov)
        if "right2" in move:
            moves.append([x, y, x - 2, y + 2])
            for mov in next_move(copy.deepcopy(board),[x, y, x - 2, y + 2]):
                moves.append(mov)
        if "left" in move:
            moves.append([x, y, x - 1, y - 1])
        if "right" in move:
            moves.append([x, y, x - 1, y + 1])
    elif figure == "w" and board[x][y] == 3:
        r_move = can_remuve_queen(board, x, y,[1,3],[2,4])
        move = can_moove_queen(board, x, y)
        for i in r_move:
            moves.append(i)
            for mov in next_move(copy.deepcopy(board),i):
                moves.append(mov)
        for i in move:
            moves.append(i)
    elif figure == "b" and board[x][y] == 4:
        r_move = can_remuve_queen(board, x, y,[2,4],[1,3])
        move = can_moove_queen(board, x, y)
        for i in r_move:
            moves.append(i)
            for mov in next_move(copy.deepcopy(board),i):
                moves.append(mov)
        for i in move:
            moves.append(i)
    return moves