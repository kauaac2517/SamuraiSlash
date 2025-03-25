import pygame.image
#from pygame import Surface, Rect


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load("./assets/background.png")
        self.surf = pygame.transform.scale(self.surf, (960, 540))
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        pygame.mixer_music.load('./assets/bgMusic.mpeg')
        pygame.mixer_music.play(-1)

        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                   pygame.quit()
                   quit()