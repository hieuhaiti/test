import pygame, os

pygame.init()

RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class Assets():
    font_big_size = pygame.font.SysFont("times", 60)
    font_small_size = pygame.font.SysFont('times', 23)

    def __init__(self, win, SCREEN_WIDTH, SCREEN_HEIGHT, BORDER_LEFT, BORDER_RIGHT):
        self.win = win
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.BORDER_LEFT = BORDER_LEFT
        self.BORDER_RIGHT = BORDER_RIGHT

    def alert(self, text):
        draw_text = Assets.font_big_size.render(text, 1, RED)
        self.win.blit(draw_text, (self.SCREEN_WIDTH / 2 - draw_text.get_width() / 2, self.SCREEN_HEIGHT / 2 - draw_text.get_height()))
        pygame.display.update()
        pygame.time.delay(2000)
        
    def status_text(self, text, value, x, y):
        text_txt = Assets.font_small_size.render(f'{text}: {value}', True, WHITE)
        if x == self.BORDER_LEFT:
            self.win.blit(text_txt,(x, y))
        if x == self.BORDER_RIGHT:
            self.win.blit(text_txt,(x - text_txt.get_width(), y))

    def load_sound(self, filename):
        SOUND = pygame.mixer.Sound(os.path.join('raw\Assets', filename))
        pygame.mixer.Sound.play(SOUND)

