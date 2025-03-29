import pygame.image
import pygame.key

from Code.constants import entitySpeed, windowWidth, windowHeight
from Code.entity import Entity


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self, ):

        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_RIGHT] and self.rect.top > 0:
            self.rect.centerx += 1

            #pygame.image.load("./assets/Entidades/Player0.png").convert_alpha()
            #self.rect.centerx += (entitySpeed)[self.name]
            #self self.rect.right <= 0:
                #self.rect.left = windowWidth

        if pressed_key[pygame.K_LEFT] and self.rect.top > 0:
            self.rect.centerx -= 1
            self.rect.centerx -= (entitySpeed)[self.name]
            if self.rect.right <= 0:
                self.rect.left = windowWidth

        if pressed_key[pygame.K_UP] and self.rect.top > 0:
            self.rect.centery -= 1
            self.rect.centerx += (entitySpeed)[self.name]
            if self.rect.right <= 0:
                self.rect.left = windowWidth

        if pressed_key[pygame.K_DOWN] and self.rect.top > 0:
            self.rect.centery += 1
            self.rect.centerx += (entitySpeed)[self.name]
            if self.rect.right <= 0:
                self.rect.left = windowWidth

        pass


