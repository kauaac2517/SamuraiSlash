import pygame.image

from pygame import Surface, Rect
from pygame.font import Font
from Code.constants import colorOrange, menuOptions, colorWhite, colorYellow


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
            self.menu_text(130, "Samurai", colorOrange, ((960 / 2), 70))
            self.menu_text(130, "Slash", colorOrange, ((960 / 2), 180))

            for i in range(len(menuOptions)):
                if i == menuOptions:
                    self.menu_text(80, menuOptions[i], colorYellow, ((960 / 2), 290 + 60 * i))
                else:
                    self.menu_text(80, menuOptions[i], colorWhite, ((960 / 2), 290 + 60 * i))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                   pygame.quit()
                   quit()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.Font('./assets/Jacquard12-Regular.ttf', size = text_size)
        #Font = pygame.font.SysFont(name = "Times New Roman", bold = True, size = text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center = text_center_pos)
        self.window.blit(source = text_surf, dest = text_rect)
