import pygame

from Code.entity import Entity
from Code.entityFactory import EntityFactory


class Gameplay:
    def __init__(self, window): #name):
        self.window = window
        self.surf = pygame.image.load("./assets/bgInGame.png")
        self.surf = pygame.transform.scale(self.surf, (960, 540))
        self.rect = self.surf.get_rect(left=0, top=0)
        #self.name = name
        #self.entity_list = list[Entity] = []
        #self.entity_list.extend(EntityFactory.get_entity("bgInGame"))

    def run(self):
       while True:
           self.window.blit(source=self.surf, dest=self.rect)
            #for ent in self.entity_list:
                #self.window.blit(source=ent.surf, dest=ent.rect)
           pygame.display.flip()
           for event in pygame.event.get():
               if event.type == pygame.QUIT:
                   pygame.quit()
                   quit()
       pass