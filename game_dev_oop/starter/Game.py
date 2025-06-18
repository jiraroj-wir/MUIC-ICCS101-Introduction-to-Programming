import pygame
from pygame.locals import *
from random import randint

from Player import Player
from Food import Food
from Scorecard import Scorecard
from Pill import Pill
from Coin import Coin


class Game:
    def __init__(self):
        # initialize pygame
        pygame.init()
        pygame.display.set_caption("ICCS101 - SNAKE")

        # timing parameters
        self.clock = pygame.time.Clock()
        self.FPS = 30
        self.gameSpeed = 3  # update player every 3 frames

        # graphics
        # the background image is 1024 × 768 px, so it should be 4:3
        self.maxX = 20
        self.maxY = 15
        self.blockSize = 40
        self.windowWidth = self.maxX * self.blockSize
        self.windowHeight = self.maxY * self.blockSize
        self.screen = pygame.display.set_mode(
            (self.windowWidth, self.windowHeight), pygame.HWSURFACE
        )
        self.bgImage = pygame.image.load("assets/bg.jpg").convert()

        self.reset()

    def get_unique_position(self, used_positions):
        while True:
            x, y = randint(0, self.maxX - 1), randint(0, self.maxY - 1)
            if (x, y) not in used_positions:
                used_positions.add((x, y))
                return x, y

    def reset(self):
        """
        Reset the game
        """
        self.player = Player(3, 3, self.blockSize, pygame.Color("red"))
        used_positions = set(self.player.body)

        fx, fy = self.get_unique_position(used_positions)
        self.food = Food(fx, fy, self.blockSize)

        px, py = self.get_unique_position(used_positions)
        self.pill = Pill(px, py, self.blockSize)

        self.coins = []
        for _ in range(5):
            cx, cy = self.get_unique_position(used_positions)
            self.coins.append(Coin(cx, cy, self.blockSize))

        self.score_card = Scorecard(0)

    def update(self):
        """
        Update vairous game objects
        """
        self.player.update()

        head_x, head_y = self.player.body[0]

        # eat food
        if (head_x, head_y) == (self.food.x, self.food.y):
            self.player.length += 1
            self.score_card.score += 100
            self.food.sound()

            used_positions = set(self.player.body)
            used_positions.add((self.pill.x, self.pill.y))
            used_positions.update((c.x, c.y) for c in self.coins)
            fx, fy = self.get_unique_position(used_positions)
            self.food = Food(fx, fy, self.blockSize)

        # eat pill
        if (head_x, head_y) == (self.pill.x, self.pill.y):
            if self.player.length >= 3:
                self.player.length -= 2
            self.score_card.score -= 50
            self.pill.sound()

            used_positions = set(self.player.body)
            used_positions.add((self.food.x, self.food.y))
            used_positions.update((c.x, c.y) for c in self.coins)
            px, py = self.get_unique_position(used_positions)
            self.pill = Pill(px, py, self.blockSize)

        # hit any coins
        head_x, head_y = self.player.body[0]
        for idx, coin in enumerate(self.coins):
            if coin.x == head_x and coin.y == head_y:
                coin.sound()
                self.score_card.score += 500

                used_positions = set(self.player.body)
                used_positions.add((self.food.x, self.food.y))
                used_positions.add((self.pill.x, self.pill.y))
                used_positions.update(
                    (c.x, c.y) for i, c in enumerate(self.coins) if i != idx
                )

                cx, cy = self.get_unique_position(used_positions)
                self.coins[idx] = Coin(cx, cy, self.blockSize)
                break  # you can only hit one coin in a single frame

        # hit the wall (die)
        if head_x < 0 or head_y < 0 or head_x >= self.maxX or head_y >= self.maxY:
            self.game_over()
            return
        # eat itself (die?)
        if (head_x, head_y) in self.player.body[1:]:
            self.game_over()
            return

        # draw
        self.screen.blit(self.bgImage, (0, 0))
        self.food.draw(self.screen)
        self.player.draw(self.screen)
        self.score_card.draw(self.screen)
        self.pill.draw(self.screen)
        for coin in self.coins:
            coin.draw(self.screen)
        pygame.display.flip()

    def run(self):
        """
        Main game loop
        """
        frame_count = 0
        # Loop forever
        while True:
            pygame.event.pump()
            keys = pygame.key.get_pressed()

            if keys[K_RIGHT]:
                self.player.moveRight()
                print("RIGHT")

            if keys[K_LEFT]:
                self.player.moveLeft()
                print("LEFT")

            if keys[K_UP]:
                self.player.moveUp()
                print("UP")

            if keys[K_DOWN]:
                self.player.moveDown()
                print("DOWN")

            # Exit the game
            if keys[K_ESCAPE]:
                break

            # update the game
            if frame_count > self.gameSpeed:
                self.update()
                frame_count = 0

            frame_count += 1

            # limit game speed
            self.clock.tick(self.FPS)

        pygame.quit()

    def game_over(self):
        print("Game over")
        self.reset()
