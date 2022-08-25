from cell import Cell
from defaults import *


class Field:
    def __init__(self, game, size=FIELD_W, c_size=CELL_S):
        self.g = game
        self.x = self.y = size
        self.c_size = c_size
        self.cells = []
        self.generation = 0
        self.population = 0
        self.reset()

    def reset(self):
        self.cells = [
            [Cell() for i in range(self.x)] for j in range(self.y)]
        self.count_all_neighbors()
        self.generation = 0
        self.population = 0

    def next_generation(self):
        self.count_all_neighbors()
        self.generation += 1
        self.population = 0
        for i in range(self.x):
            for j in range(self.y):
                cell = self.cells[j][i]
                if cell.is_alive():
                    if cell.alive_neighbors in (2, 3):
                        cell.live()
                        self.population += 1
                    else:
                        cell.die()
                else:
                    if cell.alive_neighbors == 3:
                        cell.live()
                        self.population += 1
                    else:
                        cell.die()

    def count_all_neighbors(self):
        for i in range(self.x):
            for j in range(self.y):
                self.cells[j][i].alive_neighbors = \
                    self.count_cell_neighbors(i, j)

    def count_cell_neighbors(self, x, y):
        count = 0
        for dx, dy in self.dxdy1(x, y):
            if self.in_borders(dx, dy) and self.cells[dy][dx].is_alive():
                count += 1
        return count

    def in_borders(self, x, y):
        return 0 <= x < self.x and 0 <= y < self.y

    def dxdy1(self, x, y):
        return [(x + dx, y + dy) for dx in range(-1, 2)
                for dy in range(-1, 2) if any((dx, dy))]

    def __getitem__(self, item):
        return self.cells.__getitem__(item)

    def __setitem__(self, key, value):
        return self.cells.__setitem__(key, value)

    def resize(self, field_s, cell_s):
        self.x = self.y = field_s
        self.c_size = cell_s
