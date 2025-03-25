import pygame

from Code.menu import Menu

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(960, 540))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu.run()
            pass
