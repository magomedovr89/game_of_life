import pygame as pg

from defaults import *


class UIElement:
    def __init__(self, pos):
        self.pos = pos

    def render(self, screen):
        pass


class SizedElement(UIElement):
    def __init__(self, pos, size, bg_color, filled=True):
        super().__init__(pos)
        self.bg = pg.Surface(size)
        if filled:
            self.bg.fill(bg_color)

    def render(self, screen):
        screen.blit(self.bg, self.pos)


class TextElement(SizedElement):
    def __init__(self, pos, text, color, bg, font=DEFAULT_F, **kwargs):
        self.font = font
        self.color = pg.Color(color)
        self.text = text
        self.size = font.size(text)
        super().__init__(pos, self.size, bg, **kwargs)

    def render(self, screen):
        screen.blit(self.bg, self.pos)
        screen.blit(self.font.render(self.text, True, self.color), self.pos)

    def upd_txt(self, new):
        self.text = new
        self.size = self.font.size(self.text)


class Button(TextElement):
    def __init__(self, func, text, pos, color, bg):
        self.func = func
        super().__init__(pos, text, color, bg)

    def __call__(self, *args, **kwargs):
        self.func(*args, **kwargs)

    def is_collided(self, x, y):
        return 0 <= x - self.pos[0] <= self.size[0] and \
               0 <= y - self.pos[1] <= self.size[1]
