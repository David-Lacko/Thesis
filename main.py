from bot.config import board_start
import copy
from bot.Q_learn import *
from bot.min_max import *
# from GUI.OLD import *
# from bot.Q_net import *
from bot.Q_net2 import *
nn = NN()
qlearn = Q_Learn()
win_B,win_W,tie,i,figure,running = 0,0,0,0,"w",True
def update():
    global board, figure, running, i, win_B, win_W, tie
    if board == False:
        # restart game
        i = 0
        # if figure == "w":
        #     win_B += 1
        #     print("AI win")
        # else:
        #     win_W += 1
        #     print("AI lose")
        figure = "w"
        running = False
    if figure == "w":
        figure = "b"
    else:
        figure = "w"
    i += 1
    if i == 100:
        # tie += 1
        # print("tie")
        running = False

# nn.load_model()
# qlearn.load("qlearn")
for gmaes in range(200000):
    print(gmaes)
    running = True
    board = copy.deepcopy(board_start)
    while running:
        if figure == "b":
            old_board = copy.deepcopy(board)
            board, moved = qlearn.play_move(board, figure)
            if board != False:
                qlearn.update_q_value(old_board, moved, eval_function(board, figure), board, 'w')
        else:
            old_board = copy.deepcopy(board)
            board, moved = run_random(board, figure)
            if board != False:
                qlearn.update_q_value(old_board, moved, eval_function(board, figure), board, 'b')
        update()
    if gmaes % 1000 == 0:
        qlearn.save("qlearn")
    #     nn.save_model()
# print(qlearn.q_table)
print("__________________________________________________")
print("AI win: ", win_B/1000)
print("AI lose: ", win_W/1000)
print("tie: ", tie/1000)
# nn.save_model()
# qlearn.save("qlearn")




################################################
# score, moved = min_max(copy.deepcopy(board), figure, True, 3, "deterministic")
# if moved == None:
#     board = False
# else:
#     board = make_move(board, moved)
################################################
# board, moved = run_random(board, figure)
################################################
# old_board = copy.deepcopy(board)
# board, moved = run_random(board, figure)
# if board != False:
#   qlearn.update_q_value(old_board, moved, eval_function(board, figure), board, 'b')
################################################
# board, moved = nn.move(board, figure)
# if board == False:
#     nn.learn(old_board, moved,eval_function(old_board,figure),old_board,True)
# else:
#     nn.learn(old_board, moved, eval_function(board,figure), run(copy.deepcopy(board),"w")[0], False)
