import pygame


class Text(pygame.sprite.Sprite):
    def __init__(
        self,
        size: int,
        color: pygame.Color,
        pos: tuple,
        name="Comic Sans MS",
        antialias=True,
        background_color=None,
    ) -> None:
        super().__init__()
        self.antialias = antialias
        self.color = color
        self.bg_color = background_color
        self.pos = pos
        self.font = pygame.font.SysFont(name, size)

    def show(self, display: pygame.surface.Surface, text):
        text = self.font.render(text, self.antialias, self.color, self.bg_color)
        display.blit(text, self.pos)
