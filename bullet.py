import pygame

class Bullet:
    def __init__(self, x, y):
        self.image = pygame.image.load("assets/bullet.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (20, 40))

        self.x = x
        self.y = y
        self.speed = 10

    def update(self):
        self.y -= self.speed

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))