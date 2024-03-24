import pygame
import os


class Image(pygame.sprite.Sprite):
    def __init__(self, fileName, filePath, center) -> None:
        super().__init__()
        self.image = pygame.image.load(os.path.join(filePath, "pic", fileName))
        self.rect = self.image.get_rect()
        self.rect.center = center

    def show(self, display: pygame.surface.Surface):
        return display.blit(self.image, self.rect)

    