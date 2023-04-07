import random
from bot.can_moove import *
import pickle

class Q_Learn:
    def __init__(self, alpha=0.5, gamma=0.9, exploration_rate=0.1):
        self.alpha = alpha  # learning rate
        self.gamma = gamma  # discount factor
        self.exploration_rate = exploration_rate  # exploration rate
        self.q_table = {}  # Q-table to store Q-values for each (state, action) pair

    def get_q_value(self, state, action):
        state_tuple = tuple(map(tuple, state))
        if (state_tuple, tuple(action)) not in self.q_table:
            self.q_table[(state_tuple, tuple(action))] = get_board_value(state)
        return self.q_table[(state_tuple, tuple(action))]

    def update_q_value(self, state, action, reward, next_state,next_player, end=False):
        state_tuple = tuple(map(tuple, state))
        action_tuple = tuple(action)

        next_state_tuple = tuple(map(tuple, next_state))
        next_actions = can_moove(next_state, next_player)

        current_q = self.get_q_value(state_tuple, action_tuple)
        try:
            max_next_q = max([self.get_q_value(next_state_tuple, tuple(a)) for a in next_actions])
            new_q = (1 - self.alpha) * current_q + self.alpha * (reward + self.gamma * max_next_q)
            self.q_table[(state_tuple, action_tuple)] = new_q
        except:
            max_next_q = get_board_value(next_state)
            new_q = (1 - self.alpha) * current_q + self.alpha * (reward + self.gamma * max_next_q)
            self.q_table[(state_tuple, action_tuple)] = new_q




    def choose_action(self, state,figure,moves):
        if random.random() < self.exploration_rate:
            return random.choice(moves)
        else:
            q_values = [(a, self.get_q_value(state, a)) for a in moves]
            max_q = max([q for (_, q) in q_values])
            best_actions = [a for (a, q) in q_values if q == max_q]
            return random.choice(best_actions)

    def play_move(self, state,figure):
        moves = can_moove(state, figure)
        if len(moves) == 0:
            return False, False
        action = self.choose_action(state,figure,moves)
        next_state = make_move(state, action)
        return next_state, action
    def print_q_table(self):
        print(self.q_table)

    def save(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self.q_table, f)

    def load(self, filename):
        with open(filename, 'rb') as f:
            self.q_table = pickle.load(f)
