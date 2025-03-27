import pygame

from Code.entity import Entity
from Code.entityFactory import EntityFactory


class Gameplay:
    def __init__(self, window, name):
        self.window = window
        self.name = name
        self.entity_list = list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity("bgInGame"))

    def run(self):
       while True:
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
            pygame.display.flip()
       pass