from logic import Game
import string
import random

class TetrisGame(Game):
    """ (author: demoth)
    """

    WIDTH = 30
    HEIGHT = 30

    RATE = 1

    def update(self):
        x = random.randint(0, self.WIDTH - 1)
        y = random.randint(0, self.HEIGHT - 1)
        self.screen[(x, y)] = random.choice(string.punctuation)

    def up(self, event):
        pass

    def down(self, event):
        pass

    def left(self, event):
        pass

    def right(self, event):
        pass
