import pygame
import sys
import const
from pygame.locals import *
import playerObj
import enemyObj
import textObj

pygame.init()

FramePerSec = pygame.time.Clock()
DS = pygame.display.set_mode(const.SCREEN_SIZE)
DS.fill(const.WHITE)
player = playerObj.Player()
enemy = enemyObj.Enemy()
level_info = textObj.Text(30, const.BLACK, (const.SCREEN_WIDTH-100, 0))


# endless loop for hold the game state 
while True:
    level = enemy.level
    DS.fill(const.WHITE)
    level_info.show(DS, "level:{:d}".format(level))
    enemy.moveWithFrame(drunk=True)
    player.update()
    enemy.show(DS)
    player.show(DS)
    # basic ending process 
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    # update the screen while game do some thing
    pygame.display.update()
    FramePerSec.tick(const.FPS_LIMIT)