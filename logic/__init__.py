from abc import abstractmethod, ABCMeta
__all__ = ['snake', 'tetris']

games = []

class GameMeta(ABCMeta):
    """
    """
    def __init__(cls, name, bases, namespace):
        super(GameMeta, cls).__init__(name, bases, namespace)
        if not cls.__abstractmethods__:
            games.append(cls)


class Game(metaclass=GameMeta):
    """ a game
    """
    # dimensions of screen
    WIDTH = 50
    HEIGHT = 20

    # update rate (in ms)
    RATE = 100

    def __init__(self, screen):
        self.screen = screen

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def left(self, event):
        pass

    @abstractmethod
    def right(self, event):
        pass

    @abstractmethod
    def up(self, event):
        pass

    @abstractmethod
    def down(self, event):
        pass

from logic import *
