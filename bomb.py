import pygame

class Bomb(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        #basic setup
        self.image = pygame.image.load('graphics/bomb_32x32.png').convert_alpha()
        self.rect = self.image.get_rect(center = (pos))

        #Bomb acceleration (gravity) attributes
        self.i = 0
        self.gravity = 0.25

    def apply_gravity(self):
        self.i += self.gravity
        self.rect.y += self.i

    def bomb_destroy(self):
        if self.rect.bottom > 800:
            self.kill()

    def update(self):
        self.apply_gravity()
        self.bomb_destroy()