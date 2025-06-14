import pygame


class Food:
    def __init__(self, x, y, blockSize):
        self.x = x
        self.y = y
        self.blockSize = blockSize
        self.image = pygame.image.load("assets/food.png").convert()
        self.sfx = pygame.mixer.Sound("assets/sfx1.wav")

    def draw(self, surface):
        surface.blit(self.image, (self.x * self.blockSize, self.y * self.blockSize))

    def sound(self):
        self.sfx.play()
