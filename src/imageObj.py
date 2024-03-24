import pygame
import const
import os


class Image(pygame.sprite.Sprite):
    def __init__(self, name) -> None:
        super().__init__()
        self.image = pygame.image.load(os.path.join(const.MAIN_PATH, "pic", name))
        self.rect = self.image.get_rect()

    def show(self, display: pygame.surface.Surface):
        return display.blit(self.image, self.rect)
