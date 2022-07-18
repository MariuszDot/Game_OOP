import pygame
from bomb import Bomb
from fire_balls import FireBall

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('graphics/Venom_w_samolocie_124x98.png').convert_alpha()
        self.rect = self.image.get_rect(center = (150,200))
        self.rect.inflate_ip(-30,-15)
        #moving speeds
        self.speed_x_right = 8
        self.speed_x_left = 4
        self.speed_y_top = 8
        self.speed_y_down = 8
        #bomb drop delay
        self.ready = True
        self.bomb_time = 0
        self.bomb_cooldown = 1500
        # Fire ball delay
        self.fire_ready = True
        self.fire_time = 0
        self.fire_cooldown = 700
        #Bomb adn Fire Ball setup
        self.bomb = pygame.sprite.Group()
        self.fire_ball = pygame.sprite.Group()

    #Getting Player input
    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed_x_left
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed_x_right
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed_y_top
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed_y_down
        if keys[pygame.K_SPACE] and self.ready:
            self.ready = False
            self.bomb_time = pygame.time.get_ticks()
            self.bomb.add(Bomb(self.rect.midbottom))
        if keys[pygame.K_LCTRL]and self.fire_ready:
            self.fire_ready = False
            self.fire_time = pygame.time.get_ticks()
            self.fire_ball.add(FireBall(self.rect.midbottom))

    #Recharging the Bomb
    def recharge_bomb(self):
        if not self.ready:
            current_time = pygame.time.get_ticks()
            if current_time - self.bomb_time >= self.bomb_cooldown:
                self.ready = True

    def recharge_fire(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.fire_time >= self.fire_cooldown:
            self.fire_ready = True
                
    #Constraints of the Player
    def constraints(self):
        if self.rect.right >= 900:
            self.rect.right = 900
        if self.rect.left <= 50:
            self.rect.left = 50
        if self.rect.top <= 50:
            self.rect.top = 50
        if self.rect.bottom >= 600:
            self.rect.bottom = 600

    def update(self):
        self.get_input()
        self.recharge_bomb()
        self.recharge_fire()
        self.constraints()
        self.bomb.update()
        self.fire_ball.update()
