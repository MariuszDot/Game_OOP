import pygame

class BombExplode(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y,static_dynamic,offset_x,offset_y):
        super().__init__()
        self.static_or_dynamic = static_dynamic
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.image_0 = pygame.image.load('graphics/Explosion/explosion_0_200x200.png').convert_alpha()
        self.image_1 = pygame.image.load('graphics/Explosion/explosion_1_200x200.png').convert_alpha()
        self.image_2 = pygame.image.load('graphics/Explosion/explosion_2_200x200.png').convert_alpha()
        self.image_3 = pygame.image.load('graphics/Explosion/explosion_3_200x200.png').convert_alpha()
        self.image_4 = pygame.image.load('graphics/Explosion/explosion_4_200x200.png').convert_alpha()
        self.image_5 = pygame.image.load('graphics/Explosion/explosion_5_200x200.png').convert_alpha()
        self.image_6 = pygame.image.load('graphics/Explosion/explosion_6_200x200.png').convert_alpha()
        self.image_7 = pygame.image.load('graphics/Explosion/explosion_7_200x200.png').convert_alpha()
        self.image_8 = pygame.image.load('graphics/Explosion/explosion_8_200x200.png').convert_alpha()
        self.image_9 = pygame.image.load('graphics/Explosion/explosion_9_200x200.png').convert_alpha()
        self.image_10 = pygame.image.load('graphics/Explosion/explosion_10_200x200.png').convert_alpha()
        self.image_11 = pygame.image.load('graphics/Explosion/explosion_11_200x200.png').convert_alpha()
        self.image_12 = pygame.image.load('graphics/Explosion/explosion_12_200x200.png').convert_alpha()
        self.image_13 = pygame.image.load('graphics/Explosion/explosion_13_200x200.png').convert_alpha()
        self.image_14 = pygame.image.load('graphics/Explosion/explosion_14_200x200.png').convert_alpha()
        self.image_15 = pygame.image.load('graphics/Explosion/explosion_15_200x200.png').convert_alpha()
        self.image_16 = pygame.image.load('graphics/Explosion/explosion_16_200x200.png').convert_alpha()
        self.image_17 = pygame.image.load('graphics/Explosion/explosion_17_200x200.png').convert_alpha()
        self.image_18 = pygame.image.load('graphics/Explosion/explosion_18_200x200.png').convert_alpha()
        self.image_19 = pygame.image.load('graphics/Explosion/explosion_19_200x200.png').convert_alpha()
        self.image_20 = pygame.image.load('graphics/Explosion/explosion_20_200x200.png').convert_alpha()
        self.image_21 = pygame.image.load('graphics/Explosion/explosion_21_200x200.png').convert_alpha()
        self.image_22 = pygame.image.load('graphics/Explosion/explosion_22_200x200.png').convert_alpha()
        self.frames = [self.image_0,self.image_1,self.image_2,self.image_3,self.image_4,self.image_5,self.image_6,\
        self.image_7,self.image_8,self.image_9,self.image_10,self.image_11,self.image_12,self.image_13,\
        self.image_14,self.image_15,self.image_16,self.image_17,self.image_18,self.image_19,self.image_20,\
        self.image_21,self.image_22]
        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(center = (pos_x + self.offset_x,pos_y + self.offset_y))

    def animation(self):
        self.animation_index += 0.25
        if self.animation_index >= len(self.frames) - 1:
            self.kill()
        self.image = self.frames[int(self.animation_index)]

    def dynamic(self):
        # Static or dynamic animation corresponds with static sprites or moving (dynamic) sprites !speed correlates
        # with other sprites!
        if self.static_or_dynamic == 1:
            self.rect.x -= 6

    def update(self):
        self.animation()
        self.dynamic()

