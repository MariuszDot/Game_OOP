import pygame

class RightDog(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('graphics/small_venom_350x408.png').convert_alpha()
        self.rect = self.image.get_rect(center = (1080,500))

class LeftDog(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('graphics/venom_351.png').convert_alpha()
        self.rect = self.image.get_rect(center = (210,500))

class BigDog(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('graphics/venom_ucieszona_450.png').convert_alpha()
        self.rect = self.image.get_rect(center = (640,250))