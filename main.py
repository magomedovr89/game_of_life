import pygame as pg

from game import Game

pg.init()
pg.display.set_caption('Game Of Life')

game = Game()
while True:
    game.loop()
