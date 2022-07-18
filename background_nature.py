import pygame
from random import randint, choice

class Tree(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('graphics/tree_300.png').convert_alpha()
        self.density = randint(1400,2500)
        self.rect = self.image.get_rect(midbottom = (self.density,780))

    def move(self):
        self.rect.left -= 6

    def killed(self):
        if self.rect.right < 0:
            self.kill()

    def update(self):
        self.move()
        self.killed()

class Tree2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('graphics/tree_250.png').convert_alpha()
        self.density = randint(2300,3500)
        self.rect = self.image.get_rect(midbottom = (self.density,780))

    def move(self):
        self.rect.left -= 6

    def killed(self):
        if self.rect.right < 0:
            self.kill()

    def update(self):
        self.move()
        self.killed()

class Grass(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('graphics/trawa_3000.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom = (630,800))

    def update(self,direction):
        self.rect.topleft = (self.rect.x + direction,self.rect.y)

class PowerTower(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('graphics/tower_175.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom = (randint(1300,1700),800))

    def move(self):
        self.rect.x -= 6

    def killed(self):
        if self.rect.right < 0:
            self.kill()

    def update(self):
        self.move()
        self.killed()
