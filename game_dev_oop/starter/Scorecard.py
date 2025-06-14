import pygame


class Scorecard:
    def __init__(self, initial_score):
        self.score = initial_score
        self.font = pygame.font.SysFont("Lucida Grande", 36)

    def draw(self, surface):
        color = (0, 255, 0)
        text = self.font.render("Score: {}".format(self.score), True, color)
        surface.blit(text, (0, 0))
