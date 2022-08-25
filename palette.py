from random import choice


class Palette:
    def __init__(self, *colors):
        self.colors = colors
        self.bg = colors[0]
        self.bg_el = colors[1]
        self.text = colors[2]
        self.dead = colors[3]
        self.alive = colors[4]

    def __getitem__(self, item):
        return self.colors[item]


def get_random_color(start, end):
    value = [i for i in range(start, end, 25)]
    r = choice(value)
    g = choice(value)
    b = choice(value)
    return r, g, b


def get_bright_rand_c():
    return get_random_color(100, 255)


def get_normal_rand_c():
    return get_random_color(75, 175)


def get_dark_rand_c():
    return get_random_color(0, 100)


def generate_palette():
    return Palette(get_normal_rand_c(),
                   get_bright_rand_c(),
                   get_dark_rand_c(),
                   get_dark_rand_c(),
                   get_bright_rand_c())
