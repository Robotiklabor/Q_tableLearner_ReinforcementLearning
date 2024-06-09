
import numpy as np
import pygame

class Grid:
    def __init__(self, screen_width, gridworld_map):
        self.screen_width = screen_width
        self.map = gridworld_map
        self.goal_row = np.where(self.map==6)[0][0]
        self.goal_column = np.where(self.map==6)[1][0]
        if np.any(self.map==8):
            self.pit_row = np.where(self.map==8)[0][0]
            self.pit_column = np.where(self.map==8)[1][0]
        else:
            self.pit_row = 100 #dummy values
            self.pit_column = 100 #dummy values

        #Gridsize
        self.grid_height = gridworld_map.shape[0]
        self.grid_width = gridworld_map.shape[1]
        
        self.screen_height = round(self.screen_width*(self.grid_height/self.grid_width))
        
        self.grid_block_width=round(self.screen_width/self.grid_width)
        self.grid_block_height=round(self.screen_height/self.grid_height)
        
        self.fontsize=round(self.grid_block_height*0.1)
        self.myfont = pygame.font.SysFont('arial', self.fontsize, bold=1)

class Env:
        
    def __init__(self, gridworld):
        self.grid_width = gridworld.grid_width
        self.grid_height =gridworld.grid_height
        self.goal_row = gridworld.goal_row
        self.goal_column = gridworld.goal_column
        self.pit_row = gridworld.pit_row
        self.pit_column = gridworld.pit_column
        
        self.start_row = np.where(gridworld.map==5)[0][0]
        self.start_column = np.where(gridworld.map==5)[1][0]
        self.state_row = self.start_row
        self.state_column = self.start_column
        self.next_row = 0
        self.next_column = 0
        
    def reset(self):
        self.state_row = self.start_row
        self.state_column = self.start_column
        self.next_row = 0
        self.next_column = 0
        
    def state_update(self):
        self.state_row = self.next_row
        self.state_column = self.next_column
    
    def get_state(self):
        return self.state_row, self.state_column
    
    def step(self, action):
        reward=-1
        done= False
        
        # up
        if action == 0:
            if self.state_row > 0:
                self.next_row = self.state_row -1
                self.next_column = self.state_column
            else:
                self.next_row = self.state_row   #upper border
                self.next_column = self.state_column
        # down        
        if action == 1:
            if self.state_row < self.grid_height-1:
                self.next_row = self.state_row +1
                self.next_column = self.state_column
            else:
                self.next_row = self.state_row   #lower border
                self.next_column = self.state_column
                
        # left
        if action == 2:
            if self.state_column > 0:
                self.next_column = self.state_column -1
                self.next_row = self.state_row
            else:
                self.next_column = self.state_column   #left border
                self.next_row = self.state_row
        # right        
        if action == 3:
            if self.state_column < (self.grid_width-1):
                self.next_column = self.state_column +1
                self.next_row = self.state_row
            else:
                self.next_column = self.state_column   #lower border
                self.next_row = self.state_row
    
        # finish state
        if self.next_row==self.goal_row and self.next_column==self.goal_column:
            #reward=0
            done=True

        # pit state
        if self.next_row==self.pit_row and self.next_column==self.pit_column:
            reward= -5
            done=True
        
        self.state_update()
        
        return self.next_row, self.next_column, reward, done
