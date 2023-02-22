running = True
figure = "w"
from bot.AI import *
from bot.config import bord
import copy
i = 0
nn = NN()
win_B = 0
WIN_W = 0
for run in range(1):
    print(run)
    running = True
    board = copy.deepcopy(bord)
    print(board)
    while running:
        # mive with AI
        if figure == "b":
            board, next, moved = nn.move(board, figure)
        else:
            board, next, moved = main(board, figure)

        if board == False:
            # restart game
            i = 0
            if figure == "w":
                WIN_W += 1
            else:
                win_B += 1
            figure = "w"
            running = False

        if next == False:
            if figure == "w":
                figure = "b"
            else:
                figure = "w"
        else:
            print("test")
        i += 1
        if i == 100:
            break
print("__________________________________________________")
print(win_B)
print(WIN_W)
