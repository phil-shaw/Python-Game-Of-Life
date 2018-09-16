import pygame, sys, random

from constants import *
from world import world


def copyWorld(w1, w2):

    for row in range(0, WORLD_ROWS + 2):
        for col in range(0, WORLD_COLS + 2):
            w2.setCell(row, col, w1.getCell(row, col))

def worldChanged(w1, w2):

    for row in range(0, WORLD_ROWS + 2):
        for col in range(0, WORLD_COLS + 2):
            if w1.getCell(row, col) != w2.getCell(row, col):
                return True
    return False

pygame.init()
windowSize = (SCREEN_X, SCREEN_Y)
screen = pygame.display.set_mode(windowSize)
screen.fill(BLACK)
clock = pygame.time.Clock()


world1 = world()
world1.randomWorld()


while 1:

    clock.tick(40)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    world1.showWorld(screen)
    world1.updateWorld()

    pygame.display.update()