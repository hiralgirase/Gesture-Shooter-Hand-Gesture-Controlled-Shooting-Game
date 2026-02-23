import pygame

class Player:
    def __init__(self, width, height):
        self.image = pygame.image.load("assets/player.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (60, 60))

        self.x = width // 2
        self.y = height - 80
        self.speed = 6
        self.health = 100
        self.width = width

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < self.width - 60:
            self.x += self.speed

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))