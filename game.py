import sys

import pygame as pg

from UlElement import Button, TextElement
from defaults import *
from event_handler import GameHandler
from field import Field
from palette import generate_palette
from renderer import Renderer


class Game(GameHandler):
    def __init__(self, win_s=WIN_SIZE_counted, f_size=FIELD_W, c_size=CELL_S,
                 f_offset=FIELD_OFFSET, palette=DEFAULT_PALETTE, size_ind=0,
                 fps=60):
        commands = {
            pg.K_c: self.change_colors,
            pg.K_RETURN: self.pause_resume,
            pg.K_SPACE: self.pause_resume,
            pg.K_f: self.resize,
            pg.K_r: self.reset,
            pg.K_ESCAPE: self.exit
        }
        super().__init__(commands)

        self.r = Renderer(self, win_s, f_size, c_size, f_offset, palette)
        self.field = Field(self, f_size, c_size)
        self.size_ind = size_ind

        self.buttons = []
        self.labels = []
        self.init_UI()
        self.running = False
        self.clock = pg.time.Clock()
        self.fps = fps

    def init_UI(self):
        self.buttons = [
            Button(self.pause_resume, 'Pause/resume (Space)', BUTTONS_POS[0],
                   self.r.palette.text, self.r.palette.bg_el),
            Button(self.reset, 'Restart(R)', BUTTONS_POS[1],
                   self.r.palette.text, self.r.palette.bg_el),
            Button(self.change_colors, 'Change color (C)', BUTTONS_POS[2],
                   self.r.palette.text, self.r.palette.bg_el),
            Button(self.resize, 'Resize Field (F)', BUTTONS_POS[3],
                   self.r.palette.text, self.r.palette.bg_el),
            Button(self.exit, 'Exit(Esc)', BUTTONS_POS[4],
                   self.r.palette.text, self.r.palette.bg_el)
        ]
        self.labels = [
            TextElement(
                LABELS_POS[0],
                f"Generation: {self.field.generation}",
                self.r.palette.text, self.r.palette.bg_el),
            TextElement(
                (LABELS_POS[1]),
                f"Population: {self.field.population}",
                self.r.palette.text, self.r.palette.bg_el),
            TextElement(
                LABELS_POS[2],
                "Game Of Life",
                self.r.palette.text, self.r.palette.bg_el, font=TITLE_F),
        ]

    def loop(self):
        self.handle()
        self.tick()
        self.r.render()

    def tick(self):
        self.clock.tick(self.fps)
        if self.running:
            self.field.next_generation()

    def in_field_clicked(self, x, y):
        x, y = self.get_clicked_cell_pos(x, y)
        return self.field.in_borders(x, y)

    def get_clicked_cell(self, x, y):
        x, y = self.get_clicked_cell_pos(x, y)
        return self.field[y][x]

    def get_clicked_cell_pos(self, x, y):
        x = (x - self.r.f_offset[0]) // self.r.cell_size
        y = (y - self.r.f_offset[1]) // self.r.cell_size

        return x, y

    def get_cell(self, x, y):
        return self.field.cells[y][x]

    def check_pressed(self, pos, mb_pressed):
        if self.in_field_clicked(*pos):
            to_change = self.get_clicked_cell(*pos)
            if mb_pressed[0]:
                to_change.live()
            if mb_pressed[2]:
                to_change.die()
        if self.button_clicked(pos):
            self.r.render()

    def button_clicked(self, pos):
        for b in self.buttons:
            if b.is_collided(*pos):
                b.func()
                b.render(self.r.screen)

    # Функции кнопок и быстрых клавиш

    def pause_resume(self):
        self.running = not self.running

    def reset(self):
        self.running = False
        self.field.reset()

    def resize(self):
        self.size_ind = (self.size_ind + 1) % (len(SIZES))
        field_cell = SIZES[self.size_ind]
        self.field.resize(*field_cell)
        self.reset()
        self.r.resize(*field_cell)

    def change_colors(self):
        # По-умолчанию цвета генерируются, но можно использовать и PALETTES
        # next_pallete = (PALETTES.index(self.r.palette) + 1) % (len(PALETTES))
        self.r.palette = generate_palette()  # PALETTES[next_pallete]
        self.init_UI()
        self.r.render()

    def exit(self):
        pg.quit()
        sys.exit()
