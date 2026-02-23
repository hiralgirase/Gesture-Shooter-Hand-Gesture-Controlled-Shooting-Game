import pygame
import random

class Enemy:
    def __init__(self, width):
        self.image = pygame.image.load("assets/enemy.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (60, 60))

        self.x = random.randint(0, width - 60)
        self.y = 0
        self.speed = random.randint(2, 4)

    def update(self):
        self.y += self.speed

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))