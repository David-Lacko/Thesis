from game.can_moove import *
import json


class Q_Learn:
    def __init__(self, alpha=0.5, gamma=0.9, exploration_rate=0):
        self.alpha = alpha  # learning rate
        self.gamma = gamma  # discount factor
        self.exploration_rate = exploration_rate  # exploration rate
        self.q_table = {}  # Q-table to store Q-values for each (state, action) pair

    def get_q_value(self, state, action):
        state_tuple, action_tuple = self.convert(state, action)
        if (state_tuple, action_tuple) not in self.q_table:
            self.q_table[(state_tuple, action_tuple)] = get_board_value(state)
        return self.q_table[(state_tuple, action_tuple)]

    def update_q_value(self, state, action, reward, next_state,next_player, end=False):
        state_tuple, action_tuple = self.convert(state, action)
        next_state_tuple,_ = self.convert(next_state, action)
        next_actions = need_move(next_state, next_player)


        current_q = self.get_q_value(state, action_tuple)
        try:
            max_next_q = max([self.get_q_value(next_state, tuple(a)) for a in next_actions])
            new_q = current_q + self.alpha * (reward + self.gamma * (max_next_q - current_q))
            self.q_table[(state_tuple, action_tuple)] = new_q
        except:
            max_next_q = get_board_value(next_state)
            new_q = current_q + self.alpha * (reward + self.gamma * (max_next_q - current_q))
            self.q_table[(state_tuple, action_tuple)] = new_q

    def compress_list(self,lst):
        compressed_lst = []
        for i, val in enumerate(lst):
            if val != 0:
                compressed_lst.append(i)
                compressed_lst.append(val)
        return tuple(compressed_lst)


    def convert(self, state, action):
        state = np.array(state).flatten()
        action = np.array(action).flatten()
        state_tuple = tuple( state)
        action_tuple = tuple(action)

        return self.compress_list(state_tuple), action_tuple

    def next_state(self, state, action):
        state = make_move(state, action)
        return state

    def choose_action(self, state,figure,moves):
        if random.random() < self.exploration_rate:
            return random.choice(moves)
        else:
            q_values = [(a, self.get_q_value(state, a)) for a in moves]
            max_q = max([q for (_, q) in q_values])
            best_actions = [a for (a, q) in q_values if q == max_q]
            return random.choice(best_actions)

    def play_move(self, state,figure):
        moves = need_move(state, figure)
        if len(moves) == 0:
            return False, False
        action = self.choose_action(state,figure,moves)
        next_state = make_move(state, action)
        return next_state, action

    def save(self, filename):
        q_table_str = {str(k): v for k, v in self.q_table.items()}
        with open(filename, 'w') as f:
            json.dump(q_table_str, f)

    def load(self, filename):
        with open(filename, 'r') as f:
            q_table_str = json.load(f)
        self.q_table = {eval(k): v for k, v in q_table_str.items()}


class Q_Learn2:
    def __init__(self, alpha=0.5, gamma=0.9, exploration_rate=0):
        self.alpha = alpha  # learning rate
        self.gamma = gamma  # discount factor
        self.exploration_rate = exploration_rate  # exploration rate
        self.q_table = {}  # Q-table to store Q-values for each (state, action) pair

    def get_q_value(self, state):
        state_tuple = self.convert(state)
        if state_tuple not in self.q_table:
            self.q_table[state_tuple] = get_board_value(state)
        return self.q_table[state_tuple]

    def update_q_value(self, state, action, reward, next_state,next_player, end=False):
        state_tuple = self.convert(state)
        current_q = self.get_q_value(state)
        try:
            max_next_q = self.get_q_value(next_state)
            new_q = current_q + self.alpha * (reward + self.gamma * (max_next_q - current_q))
            self.q_table[state_tuple] = new_q
        except:
            max_next_q = get_board_value(next_state)
            new_q = current_q + self.alpha * (reward + self.gamma * (max_next_q - current_q))
            self.q_table[state_tuple] = new_q

    def compress_list(self,lst):
        compressed_lst = []
        for i, val in enumerate(lst):
            if val != 0:
                compressed_lst.append(i)
                compressed_lst.append(val)
        return tuple(compressed_lst)


    def convert(self, state):
        state = np.array(state).flatten()
        state_tuple = tuple( state)

        return self.compress_list(state_tuple)


    def choose_action(self, state,figure,moves):
        if random.random() < self.exploration_rate:
            return random.choice(moves)
        else:
            q_values = {}
            for move in moves:
                temp_state = make_move(copy.deepcopy(state), move)
                q_values[tuple(move)] = self.get_q_value(temp_state)
            max_q = max([q for (_, q) in q_values.items()])
            best_actions = [a for (a, q) in q_values.items() if q == max_q]
            return random.choice(best_actions)

    def play_move(self, state,figure):
        moves = can_moove(state, figure)
        if len(moves) == 0:
            return False, False
        action = self.choose_action(state,figure,moves)
        next_state = make_move(state, action)
        return next_state, action

    def save(self, filename):
        q_table_str = {str(k): v for k, v in self.q_table.items()}
        with open(filename, 'w') as f:
            json.dump(q_table_str, f)

    def load(self, filename):
        with open(filename, 'r') as f:
            q_table_str = json.load(f)
        self.q_table = {eval(k): v for k, v in q_table_str.items()}
