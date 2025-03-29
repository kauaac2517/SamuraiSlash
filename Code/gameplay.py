import time

import pygame

from Code.constants import entitySpeed, windowWidth, windowHeight, spawn
from Code.entityFactory import EntityFactory
from Code.player import Player


class Gameplay:
    def __init__(self, window, name: str):
        self.window = window
        self.name = name
        self.surf = pygame.image.load("./assets/bgInGame.png").convert_alpha()
        self.surf = pygame.transform.scale(self.surf, (windowWidth, windowHeight))
        self.rect = self.surf.get_rect(left=0, top=0)


        self.entity_list = []
        self.entity_list.extend(EntityFactory.get_entity("Player"))


        #player = EntityFactory.get_entity("Player")
        #self.entity_list.append(player)





    def run(self):
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)
            self.window.blit(source=self.surf, dest=self.rect)

            #for ent in self.entity_list:
                #self.window.blit(source=ent.surf, dest=ent.rect)
                #ent.move()
                #self.window.blit(source=ent.surf, dest=ent.rect)


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                   pygame.quit()
                   quit()

            pygame.display.flip()
        pass

    #def menu_text(self, text_size: int, text: str, text_color: tuple):
        #text_font: Font = pygame.font.Font('./assets/Jacquard12-Regular.ttf', size = text_size)
        #text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        #text_rect: Rect = text_surf.get_rect(center = text_center_pos)
        #self.window.blit(source = text_surf, dest = text_rect)