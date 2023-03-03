import numpy as np
import random
import math
import pickle
import copy
from Board import Board


class QLearning():

    def __init__(self, alpha=0.5, gamma=0.9, exploration_rate=0.1, exploration_decay_rate=0.01, num_episodes=100000):
        self.alpha = alpha  # learning rate
        self.gamma = gamma  # discount factor
        self.exploration_rate = exploration_rate  # initial exploration rate
        self.exploration_decay_rate = exploration_decay_rate  # exploration decay rate
        self.num_episodes = num_episodes  # number of episodes to train for
        self.q_table = {}  # Q-table to store Q-values for each state-action pair

    def get_action(self, state):
        if random.uniform(0, 1) < self.exploration_rate:
            return random.choice(state.getPossibleMoves())
        else:
            q_values = [self.q_table.get(
                (tuple(state.getState()), action), 0) for action in state.getPossibleMoves()]
            max_q_value = max(q_values)
            if q_values.count(max_q_value) > 1:
                best_actions = [i for i in range(
                    len(state.getPossibleMoves())) if q_values[i] == max_q_value]
                action_index = random.choice(best_actions)
            else:
                action_index = q_values.index(max_q_value)
            return state.getPossibleMoves()[action_index]

    def train(self, env):
        for i in range(self.num_episodes):
            print(f'Epoch {i}')
            env.reset()
            state = copy.deepcopy(env)
            done = False
            while not done:
                # print(self.q_table)
                action = self.get_action(state)
                next_state, reward, done = env.step(action)
                if done:
                    break

                temp = [self.q_table.get((tuple(state.getState()), next_action), 0)
                        for next_action in next_state.getPossibleMoves()]
                #print(f'print in the temp {temp}')
                maxQNextState = max(temp)

                q_value = self.q_table.get(
                    (tuple(state.getState()), action), 0)
                new_q_value = q_value + self.alpha * \
                    (reward+self.gamma * maxQNextState - q_value)

                self.q_table[(tuple(state.getState()), action)] = new_q_value
                state = copy.deepcopy(next_state)
            self.exploration_rate *= self.exploration_decay_rate

        # now at the end we can store the values
        with open('q_table.pickle', 'wb') as f:
            pickle.dump(self.q_table, f)
