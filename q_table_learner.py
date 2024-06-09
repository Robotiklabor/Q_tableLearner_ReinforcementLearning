

import numpy as np


# =============================================================================
# Q-Table-Learning        
# =============================================================================
        
class Q_table_learner:
    
    
    def __init__(self, gridworld, learning_rate, gamma):
        # Q_table has to be defined like this, to ensure adaptability to new maps and visualization please don't change this
        self.Q_table = np.zeros((gridworld.grid_height, gridworld.grid_width, 4))
        self.learning_rate= learning_rate
        self.gamma = gamma # == discount factor
        
    def update_Q_value(self, state_row, state_column, action, next_state_row, next_state_column, reward):
        current_Q_value = self.Q_table[state_row, state_column, action]
        max_next_Q_value = np.max(self.Q_table[next_state_row, next_state_column])
        new_Q_value = current_Q_value + self.learning_rate * (reward + self.gamma * max_next_Q_value - current_Q_value)
        self.Q_table[state_row, state_column, action] = new_Q_value
    
    def choose_action(self, state_row, state_column, epsilon):
        if np.random.uniform() < epsilon:
            # exploration , where we choose a random action
            action = np.random.randint(4)
        else:
            # exploitation, where we choose the action with the maximum/highest Q-value
            action = np.argmax(self.Q_table[state_row, state_column])
        return action