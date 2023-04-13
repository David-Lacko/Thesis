from bot.can_moove import *

import random
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam

import tensorflow as tf
import copy

class NN:
    def __init__(self):
        self.action_size = 64 * 63
        self.epsilon = 0
        self.learning_rate = 0.001
        self.gamma = 0.95
        self.epsilon_min = 0.01
        self.epsilon_decay = 0.995
        self.model = self.set_model()


    def set_model(self):
        model = Sequential()
        model.add(Dense(128, input_dim=32, activation="relu"))
        model.add(Dense(256, activation="relu", kernel_initializer="glorot_uniform"))
        model.add(Dense(512, activation="relu", kernel_initializer="glorot_uniform"))
        model.add(Dense(self.action_size, activation="linear"))
        model.compile(optimizer=Adam(lr=self.learning_rate), loss="mse")
        return model

    def move(self, board, figure):
        moves = need_move(board, figure)
        if len(moves) == 0:
            return False, False
        else:
            move = self.choose_action(board, moves)
            board = make_move(board, move)
            board = change_to_queen(board)
            return board, move

    def choose_action(self, board, moves):
        if np.random.uniform() < self.epsilon:
            action = self.get_best_action(board, moves)
            return action

        else:
            action = random.choice(moves)
            return action

    def get_best_action(self, board, moves):
        state_flat = self.get_small(copy.deepcopy(board))
        q_values = self.model.predict(state_flat)[0]
        q_values = q_values.reshape((64, 63))
        best_value = -1000
        best_move = None
        for move in moves:
            index1 = move[0]*move[1]
            index2 = move[2]*move[3]
            value = q_values[index1][index2]
            if value > best_value:
                best_value = value
                best_move = move

        return best_move

    def get_small(self, board):
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

    def learn(self, state, action, reward, next_state):
        state_flat = self.get_small(copy.deepcopy(state))
        next_state_flat = self.get_small(copy.deepcopy(next_state))

        # Get Q-values for current state and next state
        q_values = self.model.predict(state_flat)
        next_q_values = self.model.predict(next_state_flat)
        q_values = q_values.reshape((64, 63))
        index1 = action[0]*action[1]
        index2 = action[2]*action[3]
        # Update Q-value for the chosen action in the current state
        q_values[index1][index2] = q_values[index1][index2] + self.learning_rate * (reward + self.gamma * (np.max(next_q_values) - q_values[index1][index2]))

        q_values = q_values.reshape((1, 4032))

        # Train the model using the current state and updated Q-values
        self.model.fit(state_flat, q_values, epochs=1, verbose=0)

        # Update epsilon
        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay

    def save_model(self):
        self.model.save("model.h5")

    def load_model(self):
        self.model = tf.keras.models.load_model("model.h5")

