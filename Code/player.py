import pygame.image
import pygame.key

from Code.constants import entitySpeed
from Code.entity import Entity


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

        self.run = [pygame.image.load(f"./assets/Entidades/Run{i}.png") for i in range(1, 8)]

        # Variáveis para controlar a animação
        self.current_frame = 0
        self.animation_speed = 10  # Quanto mais alto, mais devagar a animação
        self.counter = 0
        self.image = self.run[0]
        self.rect = self.image.get_rect(center=position)

    def move(self, ):
        #self.rect.centerx -= entitySpeed[self.name]
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_RIGHT] and self.rect.top > 0:
            self.rect.centerx += 1
            self.animate(self.run)

        if pressed_key[pygame.K_LEFT] and self.rect.top > 0:
            self.rect.centerx -= 1

        if pressed_key[pygame.K_UP] and self.rect.top > 0:
            self.rect.centery -= 1

        if pressed_key[pygame.K_DOWN] and self.rect.top > 0:
            self.rect.centery += 1
        pass

    def animate(self, direction_sprites):
        # Controla a animação (troca entre quadros)
        self.counter += 1
        if self.counter >= self.animation_speed:
            self.counter = 0
            self.current_frame += 1
            if self.current_frame >= len(direction_sprites):
                self.current_frame = 0
            self.image = direction_sprites[self.current_frame]
