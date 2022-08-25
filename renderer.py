import pygame as pg

from defaults import *


class Renderer:
    def __init__(self, game,
                 win_size=WIN_SIZE_counted,
                 f_size=FIELD_W,
                 c_size=CELL_S, f_offset=FIELD_OFFSET,
                 palette=DEFAULT_PALETTE):

        self.g = game
        self.palette = palette
        self.win_size = win_size
        self.f_offset = f_offset
        self.field_size = f_size
        self.cell_size = c_size
        self.screen = pg.display.set_mode(self.win_size, pg.HWSURFACE, 32)

    def render(self):
        self.screen.fill(self.palette.bg)
        self.render_cells()
        self.renders_buttons()
        self.render_labels()
        pg.display.flip()

    def renders_buttons(self):
        for b in self.g.buttons:
            b.render(self.screen)

    def render_cells(self):
        for i in range(self.field_size):
            for j in range(self.field_size):
                cell = self.g.get_cell(i, j)
                x, y = self.get_cell_abs_pos(i, j)
                to_color = self.palette.alive if cell.alive else self.palette.dead
                cell.color.fill(to_color)
                self.screen.blit(cell.color, (x, y))

    def render_labels(self):
        self.g.labels[0].upd_txt(f"Generation: {self.g.field.generation}")
        self.g.labels[1].upd_txt(f"Population: {self.g.field.population}")
        for lbl in self.g.labels:
            lbl.render(self.screen)

    def get_cell_abs_pos(self, i, j):
        x, y = i * self.cell_size, j * self.cell_size
        x += self.f_offset[0]
        y += self.f_offset[1]
        return x, y

    def resize(self, field_s, cell_s):
        self.field_size = field_s
        self.cell_size = cell_s
        self.render_cells()
