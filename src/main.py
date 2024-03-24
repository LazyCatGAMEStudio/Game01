import pygame
import sys
import const
from pygame.locals import *

pygame.init()

DS = pygame.display.set_mode(const.SCREEN_SIZE)
DS.fill(const.WHITE)


# endless loop for hold the game state 
while True:




    # basic ending process 
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    # update the screen while game do some thing
    pygame.display.update()