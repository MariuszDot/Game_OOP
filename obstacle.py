import pygame
from random import randint, choice

class Building(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image_1 = pygame.image.load('graphics/building_525.png').convert_alpha()
        self.image_2 = pygame.image.load('graphics/building.png').convert_alpha()
        self.image = choice([self.image_1,self.image_2])
        self.x_pos = randint(1300,1700)
        self.rect = self.image.get_rect(midbottom = (self.x_pos,800))
        self.rect.inflate_ip(-50,0)

    def move(self):
        self.rect.left -= 6

    def killed(self):
        if self.rect.right < -250:
            self.kill()

    def update(self):
        self.move()
        self.killed()