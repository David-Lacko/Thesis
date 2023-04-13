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
        self.learning_rate = 0.1
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
            action = self.get_best_action(board,moves)
            return action
        else:
            action = random.choice(moves)
            return action

    def get_best_action(self, board,moves):
        best_value = -1000
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

    def learn(self, state, reward, next_state):
        if next_state == False:
            next_state = copy.deepcopy(state)
        state_flat = self.get_small(copy.deepcopy(state))
        next_state_flat = self.get_small(copy.deepcopy(next_state))
        q_values = self.model.predict(state_flat)
        next_q_values = self.model.predict(next_state_flat)
        q_values = q_values[0] + self.learning_rate * (reward + self.gamma * (next_q_values[0] - q_values[0]))
        self.model.fit(state_flat, q_values, epochs=10, verbose=0)
        q = self.model.predict(state_flat)

        # update epsilon
        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay


    def save_model(self):
        self.model.save("modelQ2_10K.h5")

    def load_model(self):
        self.model = tf.keras.models.load_model("modelQ2_10K.h5")




