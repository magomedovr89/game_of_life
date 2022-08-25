import pygame as pg

from defaults import *


class Cell:
    def __init__(self, size=CELL_S):
        self.size = size
        self.color = pg.Surface((size, size))
        self.alive = False
        self.alive_neighbors = 0

    def die(self):
        self.alive = False
        self.alive_neighbors = 0

    def live(self):
        self.alive = True

    def is_alive(self):
        return self.alive

    def __str__(self):
        return f'Cell({"+" if self.alive else "-"})'
