import const
import pygame
import basicObj
import dataframe

class Player(basicObj.Basic):

    def __init__(self) -> None:
        super().__init__("Player.png", dataframe.DATA.get("player"))

    def controller(self):
        return pygame.key.get_pressed()

    def update(self) -> None:
        key_pressed = self.controller()

        if key_pressed[pygame.K_LEFT] and self.rect.left > 0 :
            self.goLt()

        
        if key_pressed[pygame.K_UP] and self.rect.top > 0 :
            self.goFwd()

        
        if key_pressed[pygame.K_DOWN] and self.rect.bottom < const.SCREEN_HEIGHT :
            self.goDown()

        
        if key_pressed[pygame.K_RIGHT] and self.rect.right < const.SCREEN_WIDTH :
            self.goRt()

        