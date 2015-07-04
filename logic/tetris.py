import random

from logic import Game

BLOCK = '█'

class TetrisGame(Game):
    """ (author: demoth)
    """
    WIDTH = 10
    HEIGHT = 16

    RATE = 333

    SHAPES = [
        [[1, 1], [1, 1]],
        [[1, 1, 1, 1]],
        [[1, 1, 1], [0, 1, 0]],
        [[1, 1, 0], [0, 1, 1]],
        [[0, 1, 1], [1, 1, 0]],
        [[1, 0, 0], [1, 1, 1]],
        [[0, 0, 1], [1, 1, 1]]
    ]

    def __init__(self, screen):
        super().__init__(screen)
        self.figure = self.createNewFigure()
        self.landed = [[0 for x in range(self.WIDTH)] for y in range(self.HEIGHT)]
        self.sideControl = 0

    def update(self):
        self.draw()
        self.update1()
        pass

    def up(self, event):
        pass

    def down(self, event):
        pass

    def left(self, event):
        self.sideControl = -1

    def right(self, event):
        self.sideControl = 1

    def update1(self):
        if self.collideWithBottomAndLanded():
            self.landed = [[0 for x in range(self.WIDTH)] for y in range(self.HEIGHT)]
            self.figure = self.createNewFigure()

        self.figure['left'] += self.sideControl
        if self.collideWithWallsAndLanded():
            self.figure['left'] -= self.sideControl
        self.sideControl = 0

        self.figure['top'] += 1
        if self.collideWithBottomAndLanded():
            self.figure['top'] -= 1
            self.landFigure()
            self.clearLinesAndShift()
            self.figure = self.createNewFigure()

    def clearLinesAndShift(self):
        for rowIndex, row in enumerate(self.landed):
            fullrow = True
            for colIndex, col in enumerate(row):
                if col == 0:
                    fullrow = False
            if fullrow:
                for ci in range(0, self.WIDTH):
                    for ri in range(rowIndex, 0, -1):
                        self.landed[ri][ci] = self.landed[ri - 1][ci]

    def createNewFigure(self):
        return {'top': 0, 'left': self.WIDTH // 2 - 1, 'shape': random.choice(self.SHAPES)}

    def draw(self):
        self.screen.clear()
        # draw landed
        for rowIndex, row in enumerate(self.landed):
            for colIndex, col in enumerate(row):
                if col == 1:
                    self.screen[(colIndex, rowIndex)] = BLOCK
        # draw figure
        for rowIndex, row in enumerate(self.figure['shape']):
            for colIndex, col in enumerate(row):
                if col == 1:
                    self.screen[(self.figure['left'] + colIndex, self.figure['top'] + rowIndex)] = BLOCK

    def collideWithBottomAndLanded(self):
        for rowIndex, row in enumerate(self.figure['shape']):
            for colIndex, col in enumerate(row):
                if col == 1 and (self.figure['top'] + rowIndex == self.HEIGHT
                                 or self.landed[self.figure['top'] + rowIndex][self.figure['left'] + colIndex] == 1):
                    return True

    def landFigure(self):
        for rowIndex, row in enumerate(self.figure['shape']):
            for colIndex, col in enumerate(row):
                if col == 1:
                    self.landed[self.figure['top'] + rowIndex][self.figure['left'] + colIndex] = 1

    def collideWithWallsAndLanded(self):
        for rowIndex, row in enumerate(self.figure['shape']):
            for colIndex, col in enumerate(row):
                if col == 1 and (self.figure['left'] + colIndex < 0 or self.figure['left'] + colIndex > self.WIDTH - 1
                                 or self.landed[self.figure['top'] + rowIndex][self.figure['left'] + colIndex] == 1):
                    return True
