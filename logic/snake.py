import random
from logic import Game


class Snake:
    def __init__(self, game):
        self.game = game
        self.x = game.WIDTH//2
        self.y = game.HEIGHT//2
        self.direction = (1, 0)
        self.length = 5
        self.segments = []

    def move(self):
        self.x += self.direction[0]
        self.y += self.direction[1]

        if self.x >= self.game.WIDTH:
            self.x = 0
        if self.x < 0:
            self.x = self.game.WIDTH - 1

        if self.y >= self.game.HEIGHT:
            self.y = 0
        if self.y < 0:
            self.y = self.game.HEIGHT - 1

        self.segments.append((self.x, self.y))
        while len(self.segments) > self.length:
            self.segments.pop(0)

    def eats(self, food):
        if (self.x, self.y) == (food.x, food.y):
            self.length += 1
            food.respawn()

    def draw(self, screen):
        for x, y in self.segments:
            screen[(x, y)] = '#'


class Food:
    def __init__(self, game):
        self.game = game
        self.respawn()

    def draw(self, screen):
        screen[(self.x, self.y)] = '%'

    def respawn(self):
        self.x = random.randint(0, self.game.WIDTH - 1)
        self.y = random.randint(0, self.game.HEIGHT - 1)


class SnakeGame(Game):
    """ simple snake game (authors: fonegg, sorseg)
    """

    def __init__(self, screen):
        super(SnakeGame, self).__init__(screen)
        self.snake = Snake(self)
        self.food = Food(self)

    def update(self):
        self.screen.clear()
        self.snake.move()
        self.snake.eats(self.food)
        self.snake.draw(self.screen)
        self.food.draw(self.screen)

    def left(self, event):
        # FIXME: we need to check if our previous segment obstructs new direction
        if self.snake.direction != (1, 0):
            self.snake.direction = (-1, 0)

    def right(self, event):
        if self.snake.direction != (-1, 0):
            self.snake.direction = (1, 0)

    def up(self, event):
        if self.snake.direction != (0, 1):
            self.snake.direction = (0, -1)

    def down(self, event):
        if self.snake.direction != (0, -1):
            self.snake.direction = (0, 1)
