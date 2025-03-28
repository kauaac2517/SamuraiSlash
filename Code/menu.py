import pygame.image

from pygame import Surface, Rect
from pygame.font import Font
from Code.constants import colorRed, menuOptions, colorWhite, colorYellow


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load("./assets/bgInGame.png").convert_alpha()
        self.surf = pygame.transform.scale(self.surf, (960, 540))
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        menu_options = 0
        pygame.mixer_music.load('./assets/Menu/bgMusic.mpeg')
        pygame.mixer_music.play(-1)

        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(130, "Samurai", colorRed, ((960 / 2), 70))
            self.menu_text(130, "Slash", colorRed, ((960 / 2), 180))

            for i in range(len(menuOptions)):
                if i == menu_options:
                    self.menu_text(80, menuOptions[i], colorYellow, ((960 / 2), 290 + 60 * i))
                else:
                    self.menu_text(80, menuOptions[i], colorWhite, ((960 / 2), 290 + 60 * i))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                   pygame.quit()
                   quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if menu_options < len(menuOptions) - 1:
                            menu_options +=1
                        else:
                            menu_options = 0

                    if event.key == pygame.K_UP:
                        if menu_options < len(menuOptions) - 1:
                            menu_options +=1
                        else:
                            menu_options = 0

                    if event.key == pygame.K_RETURN:
                        return menuOptions[menu_options]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.Font('./assets/Jacquard12-Regular.ttf', size = text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center = text_center_pos)
        self.window.blit(source = text_surf, dest = text_rect)
