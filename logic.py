import random

# dimensions of screen
WIDTH = 50
HEIGHT = 20

# update rate (in ms)
RATE = 100

class Snake:
    def __init__(self):
        self.x = WIDTH//2
        self.y = HEIGHT//2
        self.direction = (1, 0)
        self.length = 5
        self.segments = []

    def move(self):
        self.x += self.direction[0]
        self.y += self.direction[1]

        if self.x >= WIDTH:
            self.x = 0
        if self.x < 0:
            self.x = WIDTH - 1

        if self.y >= HEIGHT:
            self.y = 0
        if self.y < 0:
            self.y = HEIGHT - 1

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
    def __init__(self):
        self.respawn()

    def draw(self, screen):
        screen[(self.x, self.y)] = '%'

    def respawn(self):
        self.x = random.randint(0, WIDTH - 1)
        self.y = random.randint(0, HEIGHT - 1)

snake = Snake()
food = Food()

def update(screen):
    screen.clear()
    snake.move()
    snake.eats(food)
    snake.draw(screen)
    food.draw(screen)

def left(event):
    if snake.direction != (1, 0):
        snake.direction = (-1, 0)

def right(event):
    if snake.direction != (-1, 0):
        snake.direction = (1, 0)

def up(event):
    if snake.direction != (0, 1):
        snake.direction = (0, -1)

def down(event):
    if snake.direction != (0, -1):
        snake.direction = (0, 1)
