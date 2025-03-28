import pygame.key

from Code.entity import Entity

class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self, ):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_RIGHT] and self.rect.top > 0:
            self.rect.centerx += 1

        if pressed_key[pygame.K_LEFT] and self.rect.top > 0:
            self.rect.centerx -= 1

        if pressed_key[pygame.K_UP] and self.rect.top > 0:
            self.rect.centery -= 1

        if pressed_key[pygame.K_DOWN] and self.rect.top > 0:
            self.rect.centery += 1
        pass