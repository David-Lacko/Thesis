from game.can_moove import *

import random
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.optimizers import SGD
from tensorflow.keras.layers import Dense, Dropout, Flatten, Conv1D, MaxPooling2D
from tensorflow.keras.layers import Conv2D, MaxPooling1D
from tensorflow.keras.layers import BatchNormalization
from tensorflow.keras.layers import Activation
from tensorflow.keras.layers import LeakyReLU


import tensorflow as tf
import copy

class NAQNet:
    def __init__(self):
        self.action_size= 20
        self.epsilon = 0
        self.learning_rate = 0.1
        self.gamma = 0.8
        self.epsilon_min = 0.1
        self.epsilon_decay = 0.9995
        self.model = self.set_model()


    def set_model(self):
        model = Sequential()
        # model.add(Dense(262, input_dim=32, activation="relu"))
        # model.add(Dense(128, activation="relu", kernel_initializer="glorot_uniform"))
        # model.add(Dense(1, activation="sigmoid"))
        # model.compile(optimizer=SGD(lr=self.learning_rate), loss="mse")
        model.add(Dense(512, input_dim=32))
        model.add(LeakyReLU(alpha=0.1))
        model.add(BatchNormalization())
        model.add(Dropout(0.5))

        model.add(Dense(128))
        model.add(LeakyReLU(alpha=0.1))
        model.add(BatchNormalization())
        model.add(Dropout(0.5))

        model.add(Dense(32))
        model.add(LeakyReLU(alpha=0.1))

        model.add(Dense(1, activation='linear'))
        # model.add(Dense(512, input_dim=32, activation='leakyrelu'))
        # model.add(BatchNormalization())
        # model.add(Dropout(0.5))
        # model.add(Dense(128, activation='leakyrelu'))
        # model.add(BatchNormalization())
        # model.add(Dropout(0.5))
        # model.add(Dense(32, activation='leakyrelu'))
        # model.add(Dense(1, activation='linear'))

        # model.add(Dense(64, input_dim=32, activation='relu'))
        # model.add(Dense(32, activation='relu'))
        # model.add(Dense(16, activation='relu'))
        # model.add(Dense(1, activation='linear'))
        model.compile(optimizer='adam', loss='mse')
        return model

    def move(self, board, figure):
        moves = need_move(board, figure)
        if len(moves) == 0:
            return False, False
        else:
            move = self.choose_action(board,moves)
            board = make_move(board, move)
            board = change_to_queen(board)
            return board, move

    def choose_action(self, board,moves):
        if np.random.uniform() < self.epsilon:
            action = random.choice(moves)
            return action
        else:
            action = self.get_best_action(board,moves)

            return action

    def get_best_action(self, board,moves):
        best_value = float('-inf')
        best = []

        for move in moves:
            board_new = make_move(copy.deepcopy(board), move)
            bord_flat = self.get_small(board_new)
            value = self.model.predict(bord_flat)
            if value > best_value:
                best_value = value
                best = [move]
            elif value == best_value:
                best.append(move)
        return random.choice(best)

    def get_small(self,board):
        f = True
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

    def learn(self, state,m ,reward, next_state):
        if next_state == False:
            next_state = copy.deepcopy(state)
        state_flat = self.get_small(copy.deepcopy(state))
        next_state_flat = self.get_small(copy.deepcopy(next_state))
        q_values = self.model.predict(state_flat)
        next_q_values = self.model.predict(next_state_flat)
        q_values = q_values[0] + self.learning_rate * (reward + self.gamma * (next_q_values[0] - q_values[0]))
        self.model.fit(state_flat, q_values, epochs=1, verbose=0)

        # update epsilon
        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay


    def save_model(self):
        self.model.save("modelQ2_1k.h5")

    def load_model(self):
        self.model = tf.keras.models.load_model("modelQ2_1k.h5")