import pygame

from Code.menu import menu
class game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(600, 480))

    def run(self, ):
        while True:
            menu = menu(self.window)
            menu.run()
            pass
            #for event in pygame.event.get():
            #    if event.type == pygame.QUIT:
            #        pygame.quit()
            #       quit()