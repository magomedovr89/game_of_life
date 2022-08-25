from pygame import font

from palette import Palette, get_normal_rand_c

PALETTES = [
    Palette('#d6b2ca', '#c2d4de', '#7a4252', '#49150f', get_normal_rand_c()),
    Palette('#A43820', '#BA5536', '#46211A', '#693D3D', get_normal_rand_c()),
    Palette('#301B28', '#B6452C', '#523634', '#DDC5A2', get_normal_rand_c()),
    Palette('#8D230F', '#9B4F0F', '#1E434C', '#C99E10', get_normal_rand_c()),
    Palette('#AF4425', '#EBDCB2', '#561E0C', '#C9A66B', get_normal_rand_c()),
    Palette('#BC6D4F', '#9D331F', '#1E0000', '#500805', get_normal_rand_c())
]

DEFAULT_PALETTE = PALETTES[0]

SIZES = (
    (50, 10),
    (100, 5),
    (25, 20)
)
FIELD_W, CELL_S = SIZES[0]

FIELD_OFFSET = (50, 50)
WIN_SIZE = (1050, 550)
WIN_SIZE_counted = FIELD_W * CELL_S * 2 + 2 * FIELD_OFFSET[0], \
                   FIELD_W * CELL_S + FIELD_OFFSET[1]

font.init()
DEFAULT_F = font.SysFont("Impact", 25)
TITLE_F = font.SysFont('Impact', 42)

BUTTONS_POS = [
    (FIELD_W * CELL_S + 2 * FIELD_OFFSET[0], i)
    for i in range(200, 551, 50)
]

LABELS_POS = (FIELD_OFFSET[0], 15), \
             (FIELD_W * CELL_S - 2 * FIELD_OFFSET[0], 15), \
             (FIELD_W * CELL_S + 2 * FIELD_OFFSET[0], FIELD_OFFSET[1])
