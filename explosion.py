import pygame

class Explosion:
    def __init__(self, x, y):
        self.frames = [
            pygame.transform.scale(
                pygame.image.load("assets/explosion1.png").convert_alpha(),
                (80, 80)
            ),
            pygame.transform.scale(
                pygame.image.load("assets/explosion2.png").convert_alpha(),
                (80, 80)
            ),
            pygame.transform.scale(
                pygame.image.load("assets/explosion3.png").convert_alpha(),
                (80, 80)
            )
        ]

        self.index = 0
        self.timer = 0
        self.finished = False

        # Center explosion
        self.x = x - 40
        self.y = y - 40

    def update(self):
        self.timer += 1
        if self.timer % 6 == 0:
            self.index += 1

        if self.index >= len(self.frames):
            self.finished = True

    def draw(self, screen):
        if not self.finished:
            screen.blit(self.frames[self.index], (self.x, self.y))