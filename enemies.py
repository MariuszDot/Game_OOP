import pygame
from random import randint


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed = 1
        self.pos_y = randint(150,500)
        self.pos_x = randint(1300,1600)
        self.speed_x = 4
        self.speed_y = 2
        self.image_0 = pygame.image.load('graphics/enemies/enemy_0.png').convert_alpha()
        self.image_1 = pygame.image.load('graphics/enemies/enemy_1.png').convert_alpha()
        self.image_2 = pygame.image.load('graphics/enemies/enemy_2.png').convert_alpha()
        self.image_3 = pygame.image.load('graphics/enemies/enemy_3.png').convert_alpha()
        self.frames = [self.image_0,self.image_1,self.image_2,self.image_3]
        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.animation_speed = 0.1
        self.rect = self.image.get_rect(center = (self.pos_x, self.pos_y))
        self.time = round(pygame.time.get_ticks())
        self.time_interval = 1000
        self.player_damage = 100
        self.fire_damage = 50
        self.kill_player = False

    def move(self):
        self.rect.x -= self.speed_x
        current_time = int(pygame.time.get_ticks())
        if current_time >= self.time and current_time <= self.time+self.time_interval:
            self.rect.y -= self.speed_y
        if current_time > self.time + self.time_interval and current_time < self.time + 2*self.time_interval:
            self.rect.y += self.speed_y
        if current_time > self.time + 2*self.time_interval and current_time < self.time + 3*self.time_interval:
            self.rect.y -= self.speed_y
        if current_time > self.time + 3*self.time_interval and current_time < self.time + 4*self.time_interval:
            self.rect.y += self.speed_y
        if current_time > self.time + 4*self.time_interval and current_time < self.time + 5*self.time_interval:
            self.rect.y -= self.speed_y
        if current_time > self.time + 5*self.time_interval and current_time < self.time + 6*self.time_interval:
            self.rect.y += self.speed_y
        if current_time > self.time + 6*self.time_interval and current_time < self.time + 7*self.time_interval:
            self.rect.y -= self.speed_y

    def animation_state(self):
        self.animation_index += self.animation_speed
        if self.animation_index >= len(self.frames) - 1:
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def killed(self):
        if self.rect.right <= 0:
            self.kill()

    def update(self):
        self.move()
        self.animation_state()
        self.killed()


class EnemyTwo(Enemy):
    def __init__(self):
        super().__init__()
        self.image_0 = pygame.image.load('graphics/enemies/enemy_1_0.png').convert_alpha()
        self.image_1 = pygame.image.load('graphics/enemies/enemy_1_1.png').convert_alpha()
        self.image_2 = pygame.image.load('graphics/enemies/enemy_1_2.png').convert_alpha()
        self.image_3 = pygame.image.load('graphics/enemies/enemy_1_3.png').convert_alpha()
        self.image_4 = pygame.image.load('graphics/enemies/enemy_1_4.png').convert_alpha()
        self.image_5 = pygame.image.load('graphics/enemies/enemy_1_5.png').convert_alpha()
        self.image_6 = pygame.image.load('graphics/enemies/enemy_1_6.png').convert_alpha()
        self.image_7 = pygame.image.load('graphics/enemies/enemy_1_7.png').convert_alpha()
        self.image_8 = pygame.image.load('graphics/enemies/enemy_1_8.png').convert_alpha()
        self.image_9 = pygame.image.load('graphics/enemies/enemy_1_9.png').convert_alpha()
        self.image_10 = pygame.image.load('graphics/enemies/enemy_1_10.png').convert_alpha()
        self.image_11 = pygame.image.load('graphics/enemies/enemy_1_11.png').convert_alpha()
        self.image_12 = pygame.image.load('graphics/enemies/enemy_1_12.png').convert_alpha()
        self.image_13 = pygame.image.load('graphics/enemies/enemy_1_13.png').convert_alpha()
        self.image_14 = pygame.image.load('graphics/enemies/enemy_1_14.png').convert_alpha()
        self.image_15 = pygame.image.load('graphics/enemies/enemy_1_15.png').convert_alpha()
        self.image_16 = pygame.image.load('graphics/enemies/enemy_1_16.png').convert_alpha()
        self.frames = [self.image_0,self.image_1,self.image_2,self.image_3,self.image_4,self.image_5,self.image_6,
                       self.image_7,self.image_8,self.image_9,self.image_10,self.image_11,self.image_12,self.image_13,
                       self.image_14,self.image_15,self.image_16]
        self.animation_speed = 1
        self.player_damage = 400
        self.fire_damage = 100
        self.kill_player = True

class Friend(Enemy):
    def __init__(self):
        super().__init__()
        self.image_0 = pygame.image.load('graphics/enemies/friend_0.png').convert_alpha()
        self.image_1 = pygame.image.load('graphics/enemies/friend_1.png').convert_alpha()
        self.image_2 = pygame.image.load('graphics/enemies/friend_2.png').convert_alpha()
        self.image_3 = pygame.image.load('graphics/enemies/friend_3.png').convert_alpha()
        self.frames = [self.image_0,self.image_1,self.image_2,self.image_3]
        self.player_damage = -200
        self.fire_damage = 20

class ManualEnemy(Enemy):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.rect = self.image.get_rect(center=(pos_x, pos_y))
    def update(self):
        self.animation_state()

class ManualEnemyTwo(EnemyTwo):
    def __init__(self,pos_x, pos_y):
        super().__init__()
        self.rect = self.image.get_rect(center=(pos_x, pos_y))
    def update(self):
        self.animation_state()

class ManualFriend(Friend):
    def __init__(self,pos_x, pos_y):
        super().__init__()
        self.rect = self.image.get_rect(center=(pos_x, pos_y))
    def update(self):
        self.animation_state()

class FireSparks(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y):
        super().__init__()
        self.image_0 = pygame.image.load('graphics/fire_balls/sparks_0.png').convert_alpha()
        self.image_1 = pygame.image.load('graphics/fire_balls/sparks_1.png').convert_alpha()
        self.image_2 = pygame.image.load('graphics/fire_balls/sparks_2.png').convert_alpha()
        self.image_3 = pygame.image.load('graphics/fire_balls/sparks_3.png').convert_alpha()
        self.frames = [self.image_0,self.image_1,self.image_2,self.image_3]
        self.animation_index = 0
        self.animation_speed = 0.2
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(center = (pos_x, pos_y))

    def animation_state(self):
        self.animation_index += self.animation_speed
        if self.animation_index >= len(self.frames) - 1:
            self.kill()
        self.image = self.frames[int(self.animation_index)]

    def update(self):
        self.animation_state()

