import pygame
import sys
import const
from pygame.locals import *
import playerObj

pygame.init()

FramePerSec = pygame.time.Clock()
DS = pygame.display.set_mode(const.SCREEN_SIZE)
DS.fill(const.WHITE)
player = playerObj.Player()
print(player)

# endless loop for hold the game state 
while True:

    DS.fill(const.WHITE)
    player.update()
    player.show(DS)
    # basic ending process 
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    # update the screen while game do some thing
    pygame.display.update()
    FramePerSec.tick(const.FPS_LIMIT)