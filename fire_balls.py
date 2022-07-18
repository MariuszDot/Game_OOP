import pygame


class FireBall(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.speed = 8
        self.image_0 = pygame.image.load('graphics/fire_balls/fire_0.png').convert_alpha()
        self.image_1 = pygame.image.load('graphics/fire_balls/fire_1.png').convert_alpha()
        self.image_2 = pygame.image.load('graphics/fire_balls/fire_2.png').convert_alpha()
        self.image_3 = pygame.image.load('graphics/fire_balls/fire_3.png').convert_alpha()
        self.image_4 = pygame.image.load('graphics/fire_balls/fire_4.png').convert_alpha()
        self.image_5 = pygame.image.load('graphics/fire_balls/fire_5.png').convert_alpha()
        self.image_6 = pygame.image.load('graphics/fire_balls/fire_6.png').convert_alpha()
        self.image_7 = pygame.image.load('graphics/fire_balls/fire_7.png').convert_alpha()
        self.frames = [self.image_0,self.image_1,self.image_2,self.image_3,self.image_4,self.image_5,self.image_6,
                       self.image_7]
        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (pos))

    def animation_state(self):
        self.animation_index += 0.25
        if self.animation_index >= len(self.frames) - 1:
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def killed(self):
        if self.rect.left >= 1280:
            self.kill()

    def update(self):
        self.rect.centerx += self.speed
        self.animation_state()
        self.killed()

class ManualFireBall(FireBall):
    def __init__(self,pos):
        super().__init__(pos=pos)
    def update(self):
        self.animation_state()


