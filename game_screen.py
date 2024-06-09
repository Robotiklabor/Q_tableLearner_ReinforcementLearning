import pygame



def draw_grid(surface, Q, current_row, current_column, gridworld):
    for i in range(gridworld.grid_width):
        for j in range(gridworld.grid_height):
            mr= pygame.Rect(i*gridworld.grid_block_width, j*gridworld.grid_block_height, gridworld.grid_block_width, gridworld.grid_block_height)
            if Q.min() != 0:
                
                green= int(abs(255*max(Q[j,i,:])/(Q.min())))
            else:
                green=0
            #print(green)
            pygame.draw.rect(surface, (255, green ,0), mr)
            #pygame.draw.rect(surface, (255, max(Q[i,j,:]) ,0), mr)
            pygame.draw.rect(surface, (10,10,10), mr, 2)
            
            draw_text(surface, Q, i, j, gridworld)
    
    mr= pygame.Rect(current_column*gridworld.grid_block_width, current_row*gridworld.grid_block_height, gridworld.grid_block_width, gridworld.grid_block_height)
    pygame.draw.rect(surface, (100, 180, 255), mr)  
    pygame.draw.rect(surface, (10,10,10), mr, 2)
    draw_text(surface, Q, current_column, current_row, gridworld)
      
    pass

def draw_text(surface, Q, i, j, gridworld):
    ### Q-value up
    Q_text = gridworld.myfont.render(str(round(Q[j,i,0], ndigits=2)), False, (0, 0, 0))
    surface.blit(Q_text,(i*gridworld.grid_block_width+gridworld.grid_block_width/2 -Q_text.get_width()/2, j*gridworld.grid_block_height+2))
    ### Q-value down
    Q_text = gridworld.myfont.render(str(round(Q[j,i,1], ndigits=2)), False, (0, 0, 0))
    surface.blit(Q_text,(i*gridworld.grid_block_width+gridworld.grid_block_width/2 -Q_text.get_width()/2, (j+1)*gridworld.grid_block_height-Q_text.get_height()-2 ) )
    ### Q-value left
    Q_text = gridworld.myfont.render(str(round(Q[j,i,2], ndigits=2)), False, (0, 0, 0))
    surface.blit(Q_text,(i*gridworld.grid_block_width+2, j*gridworld.grid_block_height+gridworld.grid_block_height/2 -Q_text.get_height()/2))
    ### Q-value right
    Q_text = gridworld.myfont.render(str(round(Q[j,i,3], ndigits=2)), False, (0, 0, 0))
    surface.blit(Q_text,((i+1)*gridworld.grid_block_width-Q_text.get_width()-2, j*gridworld.grid_block_height+gridworld.grid_block_height/2 -Q_text.get_height()/2))
 
