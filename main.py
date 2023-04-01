running = True
figure = "w"
from bot.AI import *
from bot.config import board_start
import copy
from bot.min_max import *
# from GUI.OLD import *

i = 0
nn = NN()
win_B = 0
win_W = 0
# nn.load_model()
for gmaes in range(100):
    print(gmaes)
    running = True
    board = copy.deepcopy(board_start)
    while running:
        # mive with AI
        if figure == "b":
            # old_board = copy.deepcopy(board)
            score, moved = min_max(copy.deepcopy(board), figure, 3)
            # board, moved = run(board, figure)

            if moved == None:
                board = False
                print("AI lose")
            else:
                board = make_moves(board, moved, need_move(board, figure))
            # board, moved = nn.move(board, figure)
            # if board == False:
            #     nn.learn(old_board, moved,10,old_board,True)
            # else:
            #     nn.learn(old_board, moved, 1, board, False)
        else:
            board, moved = run(board, figure)
            if board == False:
                print("AI win")
        if board == False:
            # restart game
            i = 0
            if figure == "w":
                win_B += 1
            else:
                win_W += 1
            figure = "w"
            running = False
        if figure == "w":
            figure = "b"
        else:
            figure = "w"
        i += 1
        if i == 100:
            break
    # if gmaes % 50 == 0:
        # nn.save_model()
print("__________________________________________________")
print("AI win: ", win_B)
print("AI lose: ", win_W)
# nn.save_model()
