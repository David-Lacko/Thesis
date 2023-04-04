running = True
figure = "w"
from bot.config import board_start
import copy
from bot.min_max import *
# from GUI.OLD import *
from bot.Q_net import *
# from bot.Q_net2 import *

i = 0
nn = NN()
win_B = 0
win_W = 0
tie = 0
# nn.load_model()
for gmaes in range(1000):
    print(gmaes)
    running = True
    board = copy.deepcopy(board_start)
    while running:
        # mive with AI
        if figure == "b":
            old_board = copy.deepcopy(board)
            # score, moved = min_max(copy.deepcopy(board), figure, figure, 3, "random")
            # if moved == None:
            #     board = False
            # else:
            #     board = make_move(board, moved)

            board, moved = nn.move(board, figure)
            if board == False:
                nn.learn(old_board, moved,10,old_board,True)
            else:
                nn.learn(old_board, moved, 1, board, False)

        else:
            board, moved = run_random(board, figure)

            # score, moved = min_max(copy.deepcopy(board), figure,figure, 3, "deterministic")
            # if moved == None:
            #     board = False
            # else:
            #     board = make_move(board, moved)
        if board == False:
            # restart game
            i = 0
            if figure == "w":
                win_B += 1
                print("AI win")
            else:
                win_W += 1
                print("AI lose")
            figure = "w"
            running = False
        if figure == "w":
            figure = "b"
        else:
            figure = "w"
        i += 1
        if i == 100:
            tie += 1
            print("tie")
            break
    # if gmaes % 50 == 0:
        # nn.save_model()
print("__________________________________________________")
print("AI win: ", win_B/1000)
print("AI lose: ", win_W/1000)
print("tie: ", tie/1000)
# nn.save_model()
