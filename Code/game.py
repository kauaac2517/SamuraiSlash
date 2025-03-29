import pygame

from Code.constants import windowWidth, windowHeight, menuOptions
from Code.gameplay import Gameplay
from Code.menu import Menu

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(960, 540))

    def run(self):
        while True:
            menu = Menu(self.window)
            menuReturn = menu.run()

            if menuReturn == menuOptions[0]:
                gameplay = Gameplay(self.window,"Player")
                gameplay.run()
            elif menuReturn == menuOptions[1]:
                pygame.quit()
                quit()
