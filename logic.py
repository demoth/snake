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
            try:
                screen[(x, y)] = '#'
            except IndexError:
                print (self.segments)


snake = Snake()

def update(screen):
    screen.clear()
    snake.move()
    snake.draw(screen)

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
