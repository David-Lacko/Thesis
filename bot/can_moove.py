import random

import numpy as np


def can_moove(board, figure):
    moves = []
    nead_move = []
    for x in range(8):
        for y in range(8):
            if figure == "w" and board[x][y] == 1:
                move = can_remuve_white(board, x, y)
                if move == 22:
                    nead_move.append(str(x)+str(y)+str(x+2)+str(y+2))
                    nead_move.append(str(x)+str(y)+str(x+2)+str(y-2))
                elif move == 2 or move == -2:
                    nead_move.append(str(x)+str(y)+str(x+2)+str(y+move))
                elif move != 0:
                    if move == 11:
                        moves.append(str(x)+str(y)+(str(x+1)+str(y+1)))
                        moves.append(str(x)+str(y)+(str(x+1)+str(y-1)))
                    else:
                        moves.append(str(x)+str(y)+(str(x+1)+str(y+move)))

            elif figure == "b" and board[x][y] == 2:
                move = can_remuve_black(board, x, y)
                if move == 22:
                    nead_move.append(str(x)+str(y)+str(x-2)+str(y+2))
                    nead_move.append(str(x)+str(y)+str(x-2)+str(y-2))
                elif move == 2 or move == -2:
                    nead_move.append(str(x)+str(y)+str(x-2)+str(y+move))
                elif move != 0:
                    if move == 11:
                        moves.append(str(x)+str(y)+(str(x-1)+str(y+1)))
                        moves.append(str(x)+str(y)+(str(x-1)+str(y-1)))
                    else:
                        moves.append(str(x)+str(y)+(str(x-1)+str(y+move)))
            elif figure == "w" and board[x][y] == 3:
                move = can_remuve_white_queen(board, x, y)
                if move == []:
                    move = can_moove_queen(board, x, y)
                    for i in move:
                        moves.append(str(x)+str(y)+str(i[2])+str(i[3]))
                else:
                    for i in move:
                        nead_move.append(str(x)+str(y)+str(i[2])+str(i[3]))
            elif figure == "b" and board[x][y] == 4:
                move = can_remuve_black_queen(board, x, y)
                if move == []:
                    move = can_moove_queen(board, x, y)
                    for i in move:
                        moves.append(str(x)+str(y)+str(i[2])+str(i[3]))
                else:
                    for i in move:
                        nead_move.append(str(x)+str(y)+i)


    if len(nead_move) > 0:
        return nead_move
    return moves

def can_remuve_white(board, x, y):
    if y < 6 and y > 1 and x < 6:
        if board[x + 2][y - 2] == 0 and board[x + 2][y + 2] == 0 and \
                (board[x + 1][y - 1] == 2 or board[x + 1][y - 1] == 4) and \
                (board[x + 1][y + 1] == 2 or board[x + 1][y + 1] == 4):
            return 22
        if board[x + 2][y - 2] == 0 and (board[x + 1][y - 1] == 2 or board[x + 1][y - 1] == 4):
            return -2
        if board[x + 2][y + 2] == 0 and (board[x + 1][y + 1] == 2 or board[x + 1][y + 1] == 4):
            return 2
    elif (y == 7 or y ==6) and x < 6:
        if board[x + 2][y - 2] == 0 and (board[x + 1][y - 1] == 2 or board[x + 1][y - 1] == 4):
            return -2
    elif (y == 0 or y == 1) and x < 6:
        if board[x + 2][y + 2] == 0 and (board[x + 1][y + 1] == 2 or board[x + 1][y + 1] == 4):
            return 2
    return can_moove_white(board, x, y)

def can_moove_white(board, x, y):
    if x < 7 and y < 7 and y > 0:
        if board[x + 1][y - 1] == 0 and board[x + 1][y + 1] == 0:
            return 11
        elif board[x + 1][y - 1] == 0:
            return -1
        elif board[x + 1][y + 1] == 0:
            return 1
    elif y == 7 and x < 7:
        if board[x + 1][y - 1] == 0:

            return -1
    elif y == 0 and x < 7:
        if board[x + 1][y + 1] == 0:
            return 1
    return 0
def can_remuve_black(board, x, y):
    if y < 6 and y > 1 and x > 1:
        if board[x - 2][y - 2] == 0 and board[x - 2][y + 2] == 0 and \
                (board[x - 1][y - 1] == 1 or board[x - 1][y - 1] == 3) and \
                (board[x - 1][y + 1] == 1 or board[x - 1][y + 1] == 3):
            return 22
        if board[x - 2][y - 2] == 0 and (board[x - 1][y - 1] == 1 or board[x - 1][y - 1] == 3):
            return -2
        if board[x - 2][y + 2] == 0 and (board[x - 1][y + 1] == 1 or board[x - 1][y + 1] == 3):
            return 2
    elif (y == 7 or y ==6) and x > 1:
        if board[x - 2][y - 2] == 0 and (board[x - 1][y - 1] == 1 or board[x - 1][y - 1] == 3):
            return -2
    elif (y == 0 or y == 1) and x > 1:
        if board[x - 2][y + 2] == 0 and (board[x - 1][y + 1] == 1 or board[x - 1][y + 1] == 3):
            return 2
    return can_moove_black(board, x, y)

def can_moove_black(board, x, y):
    if x > 0 and y < 7 and y > 0:
        if board[x - 1][y - 1] == 0 and board[x - 1][y + 1] == 0:
            return 11
        elif board[x - 1][y - 1] == 0:
            return -1
        elif board[x - 1][y + 1] == 0:
            return 1
    elif y == 7 and x > 0:
        if board[x - 1][y - 1] == 0:
            return -1
    elif y == 0 and x > 0:
        if board[x - 1][y + 1] == 0:
            return 1
    return 0

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

def can_remuve_white_queen(board, x, y):
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
            if board[x + i][y - i] == 1 or board[x + i][y - i] == 3:
                break
            elif board[x + i][y - i] == 2 or board[x + i][y - i] == 4:
                if board[x + i + 1][y - i - 1] == 0:
                    max_move.append(str(x)+str(y)+str(x+i+1)+str(y-i-1))
                break
    if top_right > 1:
        for i in range(1, top_right):
            if board[x + i][y + i] == 1 or board[x + i][y + i] == 3:
                break
            elif board[x + i][y + i] == 2 or board[x + i][y + i] == 4:
                if board[x + i + 1][y + i + 1] == 0:
                    max_move.append(str(x)+str(y)+str(x+i+1)+str(y+i+1))
                break
    if bottom_left > 1:
        for i in range(1, bottom_left):
            if board[x - i][y - i] == 1 or board[x - i][y - i] == 3:
                break
            elif board[x - i][y - i] == 2 or board[x - i][y - i] == 4:
                if board[x - i - 1][y - i - 1] == 0:
                    max_move.append(str(x)+str(y)+str(x-i-1)+str(y-i-1))
                break
    if bottom_right > 1:
        for i in range(1, bottom_right):
            if board[x - i][y + i] == 1 or board[x - i][y + i] == 3:
                break
            elif board[x - i][y + i] == 2 or board[x - i][y + i] == 4:
                if board[x - i - 1][y + i + 1] == 0:
                    max_move.append(str(x)+str(y)+str(x-i-1)+str(y+i+1))
                break
    return max_move

def can_remuve_black_queen(board, x, y):
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
            if board[x + i][y - i] == 2 or board[x + i][y - i] == 4:
                break
            elif board[x + i][y - i] == 1 or board[x + i][y - i] == 3:
                if board[x + i + 1][y - i - 1] == 0:
                    max_move.append(str(x)+str(y)+str(x+i+1)+str(y-i-1))
                break
    if top_right > 1:
        for i in range(1, top_right):
            if board[x + i][y + i] == 2 or board[x + i][y + i] == 4:
                break
            elif board[x + i][y + i] == 1 or board[x + i][y + i] == 3:
                if board[x + i + 1][y + i + 1] == 0:
                    max_move.append(str(x)+str(y)+str(x+i+1)+str(y+i+1))
                break
    if bottom_left > 1:
        for i in range(1, bottom_left):
            if board[x - i][y - i] == 2 or board[x - i][y - i] == 4:
                break
            elif board[x - i][y - i] == 1 or board[x - i][y - i] == 3:
                if board[x - i - 1][y - i - 1] == 0:
                    max_move.append(str(x)+str(y)+str(x-i-1)+str(y-i-1))
                break
    if bottom_right > 1:
        for i in range(1, bottom_right):
            if board[x - i][y + i] == 2 or board[x - i][y + i] == 4:
                break
            elif board[x - i][y + i] == 1 or board[x - i][y + i] == 3:
                if board[x - i - 1][y + i + 1] == 0:
                    max_move.append(str(x)+str(y)+str(x-i-1)+str(y+i+1))
                break
    return max_move


def select_random_move(moves):
    if len(moves) > 0:
        return random.choice(moves)
    return 0

def make_move(board, move):
    x1 = int(move[0])
    y1 = int(move[1])
    x2 = int(move[2])
    y2 = int(move[3])
    board[x2][y2] = board[x1][y1]
    board[x1][y1] = 0
    board = remuve_skiped(board, x1, y1, x2, y2)
    if abs(x2-x1) >= 2:
        next = next_move(board, x2, y2)
        return board,next

    return board,False

def next_move(board, x2, y2):
    if board[x2][y2] == 1:
        move = can_remuve_white(board, x2, y2)
    if board[x2][y2] == 2:
        move = can_remuve_black(board, x2, y2)
    if board[x2][y2] == 3:
        move = can_remuve_white_queen(board, x2, y2)
        if move != []:
            return True
    if board[x2][y2] == 4:
        move = can_remuve_black_queen(board, x2, y2)
        if move != []:
            return True
    if move == 22 or move == 2 or move == -2:
        return True
    return False

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
    moves = can_moove(board, figure)
    move = select_random_move(moves)
    next = False
    if move != 0:
        board, next = make_move(board, move)
    else:
        return False, False, False
    board = change_to_queen(board)
    return board, next, move
