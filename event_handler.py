import sys

import pygame as pg


class EventHandler:
    def handle(self):
        pass


class CommandHandler(EventHandler):
    def __init__(self, k_c):
        self.key_commands = k_c

    def handle(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key in self.key_commands:
                    command = self.key_commands[event.key]
                    command()


class GameHandler(CommandHandler):
    def __init__(self, k_c):
        super().__init__(k_c)

    def handle(self):
        super(GameHandler, self).handle()
        mb_pressed = pg.mouse.get_pressed()
        if any(mb_pressed):
            self.check_pressed(pg.mouse.get_pos(), mb_pressed)

    def check_pressed(self, *args):
        pass
