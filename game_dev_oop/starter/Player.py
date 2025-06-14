import pygame

from pygame import Rect, Color

UP = 2
DOWN = 3
LEFT = 1
RIGHT = 0


class Player:
    def __init__(self, x, y, blockSize, color):
        self.body = [(x, y)]
        self.length = len(self.body)
        self.direction = RIGHT
        self.blockSize = blockSize
        self.color = color

    def draw(self, surface):
        """
        How the snake looks
        """
        for x, y in self.body:
            surface.fill(
                self.color,
                Rect(
                    x * self.blockSize,
                    y * self.blockSize,
                    self.blockSize,
                    self.blockSize,
                ),
            )

    def update(self):
        head_x, head_y = self.body[0]
        if self.direction == RIGHT:
            self.body.insert(0, (head_x + 1, head_y))
        if self.direction == LEFT:
            self.body.insert(0, (head_x - 1, head_y))
        if self.direction == UP:
            self.body.insert(0, (head_x, head_y - 1))
        if self.direction == DOWN:
            self.body.insert(0, (head_x, head_y + 1))
        # shrink the snake if needed
        if len(self.body) > self.length:
            self.body = self.body[: self.length]

    def moveRight(self):
        if self.direction in [UP, DOWN]:
            self.direction = RIGHT

    def moveLeft(self):
        if self.direction in [UP, DOWN]:
            self.direction = LEFT

    def moveUp(self):
        if self.direction in [LEFT, RIGHT]:
            self.direction = UP

    def moveDown(self):
        if self.direction in [LEFT, RIGHT]:
            self.direction = DOWN
