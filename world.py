from constants import *

import random
import pygame

class world:

    def __init__(self):
        self.world = [[0 for row in range(WORLD_ROWS + 2)] for row in range(WORLD_COLS + 2)]
        self.changed = None
        self.generateWorld()

    def randomWorld(self):
        random.seed()
        for row in range(1, WORLD_ROWS + 1):
            for col in range(1, WORLD_COLS + 1):
                self.world[row][col] = random.randint(0,1)

    def generateWorld(self):
        for row in range(1, WORLD_ROWS + 1):
            for col in range(1, WORLD_COLS + 1):
                self.world[row][col] = 0

    def showWorld(self, screen):
        self.screen = screen
        for row in range(0, WORLD_ROWS + 2):
            for col in range(0, WORLD_COLS + 2):
                plotX = row * 12 + 50
                plotY = col * 12 + 50
                if self.world[row][col] == 1:
                    pygame.draw.circle(self.screen, GREEN, (plotX, plotY), 6, 0)
                else:
                    pygame.draw.circle(self.screen, RED, (plotX, plotY), 6, 0)

    def getCell(self, x, y):
        return self.world[x][y]

    def setCell(self, x, y, state):
            self.world[x][y] = state

    def updateWorld(self):
        tempWorld = world()
        neighbours = 0
        self.changed = False

        for c_row in range(1, WORLD_ROWS + 1):
            for c_col in range(1, WORLD_COLS + 1):
                if self.getCell(c_row - 1, c_col - 1) == 1:
                    neighbours += 1
                if self.getCell(c_row - 1, c_col) == 1:
                    neighbours += 1
                if self.getCell(c_row - 1, c_col + 1) == 1:
                    neighbours += 1

                if self.getCell(c_row, c_col - 1) == 1:
                    neighbours += 1
                if self.getCell(c_row, c_col + 1) == 1:
                    neighbours += 1

                if self.getCell(c_row + 1, c_col - 1) == 1:
                    neighbours += 1
                if self.getCell(c_row + 1, c_col) == 1:
                    neighbours += 1
                if self.getCell(c_row + 1, c_col + 1) == 1:
                    neighbours += 1

                # If cell lives check to see if it lives on
                if self.getCell(c_row, c_col) == 1:
                    if neighbours < 2:
                        tempWorld.setCell(c_row, c_col, 0)
                    if neighbours == 2:
                        tempWorld.setCell(c_row, c_col, 1)
                    if neighbours == 3:
                        tempWorld.setCell(c_row, c_col, 1)
                    if neighbours > 3:
                        tempWorld.setCell(c_row, c_col, 0)

                # If Cell is dead but has 3 Neighbours it lives
                if self.getCell(c_row, c_col) == 0:
                    if neighbours == 3:
                        tempWorld.setCell(c_row, c_col, 1)

                neighbours = 0

        # Copy the Tempp world back to our game World
        for row in range(0, WORLD_ROWS + 2):
            for col in range(0, WORLD_COLS + 2):
                if tempWorld.getCell(row, col) != self.getCell(row, col):
                    self.changed = True
                self.setCell(row, col, tempWorld.getCell(row, col))


    def hasChanged(self):
        return self.changed