import pygame
from random import randint
from bomb_explode import BombExplode

class BadTower(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('graphics/bad_guys_tower.png').convert_alpha()
        self.pos_x = randint(1400,1650)
        self.rect = self.image.get_rect(midbottom = (self.pos_x, 780))

    def move(self):
        self.rect.left -= 6

    def killed(self):
        if self.rect.right < 0:
            self.kill()

    def update(self):
        self.move()
        self.killed()