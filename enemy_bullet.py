import pygame

class EnemyBullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 6

    def update(self):
        self.y += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 0), (self.x, self.y, 5, 10))