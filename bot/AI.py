# deep QNetwork
from bot.can_moove import *

import random
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import SGD

import tensorflow as tf
import copy

class NN:
    def __init__(self):
        self.action_size= 20
        self.epsilon = 0.9
        self.model = self.set_model()
        self.learning_rate = 0.01
        self.gamma = 0.95
        self.epsilon_min = 0.1
        self.epsilon_decay = 0.995

    def set_model(self):
        model = Sequential()
        model.add(Dense(262, input_dim=32, activation="relu"))
        model.add(Dense(128, activation="relu", kernel_initializer="glorot_uniform"))
        model.add(Dense(1, activation="sigmoid"))
        model.compile(optimizer=SGD(lr=0.01), loss="mse")
        return model

    def move(self, board, figure):
        print(board, figure)
        moves = can_moove(board, figure)
        if len(moves) == 0:
            return False, False, False
        else:
            action = self.choose_action(board,moves)
            board, next = make_move(board, action)
            board = change_to_queen(board)
            return board, next, action

    def choose_action(self, board,moves):
        if np.random.uniform() < self.epsilon:
            # choose best action
            action = self.get_best_action(board,moves)
            #random action
            # action = random.choice(moves)
            # self.learn(board, figure, action)
            return action

        else:
            action = random.choice(moves)
            # self.learn(board, figure, action)
            return action

    def get_best_action(self, board,moves):
        best_value = -1000
        for move in moves:
            board_new = make_move(copy.deepcopy(board), move)[0]
            print(board_new)
            bord_flat = self.get_small(board_new)
            value = self.model.predict(bord_flat)
            if value > best_value:
                best_value = value
                best_move = move
        print("best move", best_move)
        return best_move

    def get_small(self,board):
        f = False
        for x in range(len(board)):
            if f:
                board[x] = [x for i, x in enumerate(board[x]) if i % 2 == 0]
                f = False
            else:
                board[x] = [x for i, x in enumerate(board[x]) if i % 2 == 1]
                f = True
        bord = np.array(board)
        bord = bord.flatten()
        return bord.reshape((1, 32))



    def learn(self,board,action):
        board = make_move(board, action)
        self.model.fit(board, 1, epochs=1, verbose=0)
        return board













