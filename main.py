

# =============================================================================
# Tabular Q-Learning in Gridworld-Environment
# =============================================================================


import numpy as np
import pygame, sys
from game_screen import draw_grid
from env import Env, Grid
from q_table_learner import Q_table_learner


def main():
    # =============================================================================
    # some pygame codelines for the visualization - please don't edit except for screen_width possibly
    # =============================================================================
    screen_width=800
    screen_refresh_time = 10 # mil secs
    pygame.init()
    
    # Map for gridworld can be changed if you want
    gridworld_map = np.array([[6,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,5]]) # 1=regular field; 6=goal; 5=start
    #gridworld_map = np.array([[1,1,1,5,1,1,1,1,1,6]]) # 1=regular field; 6=goal; 5=start  
    
    gridworld = Grid(screen_width, gridworld_map )  #create gridworld object
    surface = pygame.display.set_mode(( gridworld.screen_width, gridworld.screen_height))   #create game surface
    pygame.display.set_caption("Small_Gridworld-Q-Learning")
    visuals_on =  True

    #Init
    #create Agent
    learning_rate = 0.5  # Learning rate (alpha)
    gamma = 1.0  # Discount factor (gamma)
    agent = Q_table_learner(gridworld, learning_rate, gamma) # the gridworld-object is used for the q-value representation, please don't remove this
    
    #create environment object
    env = Env(gridworld)
    
    # No of episodes to train
    no_of_episodes_to_train = 500
    # Episode counter
    current_episode = 0
    
    # =============================================================================
    # Training-(display) loop
    # =============================================================================
    ## Agent start state : Lower right corner
    ## Agent goal state : Upper left corner
    # Main loop:
    while True:
        for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            pygame.quit()
                            sys.exit()


        # execute training episode if the predefined number of episodes is not yet reached.
        if current_episode <= no_of_episodes_to_train:
    
            # Complete code here
            
            # Reset episode- (environment, rewards, done,  etc.)
            env.reset()
            # slowly reduce exploration probability epsilon
            epsilon = 1.0 / (current_episode + 1)

            # every episode execute steps in environment until termination
            while True:
                # choosing action epsilon-greedy
                state_row, state_column = env.get_state()
                action = agent.choose_action(state_row, state_column, epsilon)
                # Take a step in the environment
                [next_row, next_column, reward, done] = env.step(action)
                 # do Update for Q(s,a)
                agent.update_Q_value(state_row, state_column, action, next_row, next_column, reward)
                 # update the current state
                env.state_update()

                
    # =============================================================================
    #             Visualization should be executed after every step - please do not change
    # =============================================================================
                if visuals_on:
                    draw_grid(surface, agent.Q_table, env.state_row, env.state_column, gridworld)
                    pygame.display.update()
                    pygame.time.delay(screen_refresh_time)

                if done:
                    break
        # increment Episode-counter after each episode
        current_episode += 1


if __name__=='__main__':
    main()