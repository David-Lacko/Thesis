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
        moves = need_move(board, figure)
        # if len(moves) == 0:
        #     print('no moves')
        #     moves = can_moove(board, figure)
        if len(moves) == 0:
            return False, False
        else:
            move = self.choose_action(board,moves)
            board = make_moves(board, move, moves)
            board = change_to_queen(board)
            return board, move

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
            board_new = make_moves(copy.deepcopy(board), move,copy.deepcopy(moves))
            # print(board_new)
            bord_flat = self.get_small(board_new)
            value = self.model.predict(bord_flat)
            if value > best_value:
                best_value = value
                best_move = move
        return best_move

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

    def learn(self, state, action, reward, next_state, done):
        state_flat = self.get_small(copy.deepcopy(state))
        next_state_flat = self.get_small(copy.deepcopy(next_state))
        target = reward

        if not done:
            # compute the target value using the Q-learning update rule
            #q_values = self.model.predict(next_state_flat)[0]
            #next_action = self.get_best_action(next_state, need_move(next_state, 'w'))
            next_q_value = self.model.predict(next_state_flat)[0]
            target += self.gamma * next_q_value

        # update the Q-value for the chosen action in the current state
        target_q_values = self.model.predict(state_flat)
        target_q_values[0] = target

        # train the model using the current state and the updated target Q-values
        self.model.fit(state_flat, target_q_values, epochs=1, verbose=0)

        # update epsilon
        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay


    def save_model(self):
        self.model.save("model.h5")

    def load_model(self):
        self.model = tf.keras.models.load_model("model.h5")













