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

    def draw(self, screen):
        for x, y in self.segments:
            screen[(x, y)] = '#'

class Food:
    def __init__(self):
        self.x = random.randint(0, WIDTH - 1)
        self.y = random.randint(0, HEIGHT - 1)

    def draw(self, screen):
        screen[(self.x, self.y)] = '%'

snake = Snake()
food = Food()

def update(screen):
    screen.clear()
    snake.move()
    snake.draw(screen)
    food.draw(screen)
    if (snake.x == food.x) and (snake.y == food.y):
        food.x = random.randint(0, WIDTH - 1)
        food.y = random.randint(0, HEIGHT - 1)
        snake.length += 1

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
