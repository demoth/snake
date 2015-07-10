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
        self.figure = self.create_new_figure()
        self.landed = [[0 for x in range(self.WIDTH)] for y in range(self.HEIGHT)]
        self.side_control = 0

    def update(self):
        self.draw()
        self.update1()
        pass

    def up(self, event):
        pass

    def down(self, event):
        pass

    def left(self, event):
        self.side_control = -1

    def right(self, event):
        self.side_control = 1

    def update1(self):
        if self.collide_with_bottom_and_landed():
            self.landed = [[0 for x in range(self.WIDTH)] for y in range(self.HEIGHT)]
            self.figure = self.create_new_figure()

        self.figure['left'] += self.side_control
        if self.collide_with_walls_and_landed():
            self.figure['left'] -= self.side_control
        self.side_control = 0

        self.figure['top'] += 1
        if self.collide_with_bottom_and_landed():
            self.figure['top'] -= 1
            self.land_figure()
            self.clear_lines_and_shift()
            self.figure = self.create_new_figure()

    def clear_lines_and_shift(self):
        for row_index, row in enumerate(self.landed):
            full_row = True
            for colIndex, col in enumerate(row):
                if col == 0:
                    full_row = False
            if full_row:
                for ci in range(0, self.WIDTH):
                    for ri in range(row_index, 0, -1):
                        self.landed[ri][ci] = self.landed[ri - 1][ci]

    def create_new_figure(self):
        return {'top': 0, 'left': self.WIDTH // 2 - 1, 'shape': random.choice(self.SHAPES)}

    def draw(self):
        self.screen.clear()
        # draw landed
        for row_index, row in enumerate(self.landed):
            for col_index, col in enumerate(row):
                if col == 1:
                    self.screen[(col_index, row_index)] = BLOCK
        # draw figure
        for row_index, row in enumerate(self.figure['shape']):
            for col_index, col in enumerate(row):
                if col == 1:
                    self.screen[(self.figure['left'] + col_index, self.figure['top'] + row_index)] = BLOCK

    def collide_with_bottom_and_landed(self):
        for row_index, row in enumerate(self.figure['shape']):
            for col_index, col in enumerate(row):
                if col == 1 and (self.figure['top'] + row_index == self.HEIGHT
                                 or self.landed[self.figure['top'] + row_index][self.figure['left'] + col_index] == 1):
                    return True

    def land_figure(self):
        for row_index, row in enumerate(self.figure['shape']):
            for col_index, col in enumerate(row):
                if col == 1:
                    self.landed[self.figure['top'] + row_index][self.figure['left'] + col_index] = 1

    def collide_with_walls_and_landed(self):
        for row_index, row in enumerate(self.figure['shape']):
            for col_index, col in enumerate(row):
                if col == 1 and (self.figure['left'] + col_index < 0 or self.figure['left'] + col_index > self.WIDTH - 1
                                 or self.landed[self.figure['top'] + row_index][self.figure['left'] + col_index] == 1):
                    return True
