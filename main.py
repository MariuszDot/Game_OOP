import pygame, sys
from random import choice
from player import Player
from bomb import Bomb
from two_dogs import LeftDog, RightDog, BigDog
from bomb_explode import BombExplode
from background_nature import Tree, Tree2, Grass, PowerTower
from obstacle import Building
from static_enemy import BadTower
from enemies import Enemy, EnemyTwo, Friend, FireSparks, ManualEnemy, ManualEnemyTwo, ManualFriend
from fire_balls import ManualFireBall

class Game:
    def __init__(self,screen, score):
        self.screen = screen
        # self.game_stage = 1
    # Whole background setup
        self.background_sky = pygame.image.load('graphics/blue_sky_800_2.jpg').convert_alpha()
        self.background_sky_rect = self.background_sky.get_rect(midbottom = (screen_width/2,800))
        self.grass = pygame.sprite.GroupSingle()
        self.grass.add(Grass())
        self.grass_direction = -1
        # Trees and power towers
        self.bg_trees = pygame.sprite.Group()
        self.tree_1_density = 3
        self.tree_2_density = 1
        power_tower_sprite = PowerTower()
        self.power_tower = pygame.sprite.Group()
        self.tower_density = 1
        # Buildings
        self.building = pygame.sprite.Group()
        # Bad guys towers
        self.bad_tower = pygame.sprite.Group()
        # Enemies setup
        self.enemy = pygame.sprite.Group()

        #Player setup
        # player_sprite = Player()
        self.player = pygame.sprite.GroupSingle()
        self.player.add(Player())

        #Animations setup
        self.bomb_exploded = pygame.sprite.Group()
        self.sparks = pygame.sprite.Group()
        self.time = pygame.time.get_ticks()

        # Score
        self.font = pygame.font.Font('fonts/Amatic-Bold.ttf', 50)
        self.score = score
        self.lives = 3
        self.score_bad_tower = 100
        self.score_bomb_building = 1000
        self.score_player_building = 1000
        # Sounds
        self.explosion_music = pygame.mixer.Sound('audio/explosion07.wav')
        self.explosion_music.set_volume(0.5)
        self.bird_sound = pygame.mixer.Sound('audio/birds.wav')
        self.bird_sound.set_volume(0.3)
        self.bg_music = pygame.mixer.Sound('audio/achievement.mp3')
        self.bg_music.set_volume(0.3)
        self.bg_music.play(loops= -1)

    def trees(self):
        for _ in range(self.tree_1_density):
            self.bg_trees.add(Tree())
        for _ in range(self.tree_2_density):
            self.bg_trees.add(Tree2())

    def power_tower_setup(self):
        for _ in range(self.tower_density):
            self.power_tower.add(PowerTower())

    def building_setup(self):
        for _ in range(1):
            self.building.add(Building())

    def bad_guys_tower(self):
        for _ in range(1):
            self.bad_tower.add(BadTower())

    def enemy_setup(self):
        self.enemy.add(Enemy(),EnemyTwo(),Enemy(),Friend(),Friend())

    def grass_position_checker(self):
        if self.grass.sprite.rect.left <= -900:
            self.grass_direction = 1
        elif self.grass.sprite.rect.right >= 2150:
            self.grass_direction = -1

    def collisions(self):
        # instruction: Sprite1 VS Sprite = sprite1_sprite
        player_building = pygame.sprite.groupcollide(self.player,self.building, False, False)
        for sprite_0 in player_building:
            if player_building[sprite_0]:
                explosion_x = sprite_0.rect.x
                explosion_y = sprite_0.rect.y
                self.bomb_exploded.add(BombExplode(explosion_x,explosion_y, 1, 110, 0))
                self.player.add(Player())
                self.score -= self.score_player_building
                self.lives -= 1
                self.explosion_music.play()
        player_enemy = pygame.sprite.groupcollide(self.enemy, self.player, True, False)
        for enemy in player_enemy:
            if player_enemy[enemy]:
                sparks_x = enemy.rect.x + 80
                sparks_y = enemy.rect.y
                self.sparks.add(FireSparks(sparks_x,sparks_y))
                self.score -= enemy.player_damage
                self.bird_sound.play()
                if enemy.kill_player:
                    self.lives -= 1

        bomb_grass = pygame.sprite.groupcollide(self.player.sprite.bomb, self.grass, True, False)
        for sprite in bomb_grass:
            if bomb_grass[sprite]:
                explosion_x = sprite.rect.x
                explosion_y = sprite.rect.y
                self.bomb_exploded.add(BombExplode(explosion_x,explosion_y, 1, 0, 35))
                self.explosion_music.play()
        bomb_building = pygame.sprite.groupcollide(self.player.sprite.bomb, self.building, True, False)
        for sprite_1 in bomb_building:
            if bomb_building[sprite_1]:
                explosion_x = sprite_1.rect.x
                explosion_y = sprite_1.rect.y
                self.bomb_exploded.add(BombExplode(explosion_x,explosion_y, 1, 40,0))
                self.score -= self.score_bomb_building
                self.explosion_music.play()
        bomb_badtower = pygame.sprite.groupcollide(self.player.sprite.bomb, self.bad_tower, False, True)
        if bomb_badtower:
            self.score += self.score_bad_tower
        fire_enemy = pygame.sprite.groupcollide(self.enemy, self.player.sprite.fire_ball, True, False)
        for sprite_2 in fire_enemy:
            if fire_enemy[sprite_2]:
                sparks_x = sprite_2.rect.x + 50
                sparks_y = sprite_2.rect.y
                self.sparks.add(FireSparks(sparks_x, sparks_y))
                self.score += sprite_2.fire_damage
                self.bird_sound.play()

    def display_score(self):
        score_surf = self.font.render(f'Score: {self.score}', True, (0, 0, 102))
        score_rect = score_surf.get_rect(center = (530,50))
        self.screen.blit(score_surf,score_rect)

    def display_lives(self):
        self.dog_face_surf = pygame.image.load('graphics/venom_ucieszona_450.png').convert_alpha()
        self.dog_face_surf = pygame.transform.rotozoom(self.dog_face_surf, 0, 0.2)
        self.dog_face_rect = self.dog_face_surf.get_rect(center = (730, 50))
        self.screen.blit(self.dog_face_surf,self.dog_face_rect)
        self.lives_text_surf = self.font.render(f'X {self.lives}', True, (0, 0, 102))
        self.lives_text_rect = self.lives_text_surf.get_rect(center = (795, 50))
        self.screen.blit(self.lives_text_surf, self.lives_text_rect)

    def run(self):
        # Updates, background
        self.screen.blit(self.background_sky,self.background_sky_rect)
        self.bg_trees.update()
        self.power_tower.update()
        self.player.update()
        self.building.update()
        self.grass.update(self.grass_direction)
        self.bomb_exploded.update()
        self.bad_tower.update()
        self.enemy.update()
        self.sparks.update()
        self.display_score()
        self.display_lives()

        # Draw things
        self.power_tower.draw(self.screen)
        self.player.draw(self.screen)
        self.player.sprite.bomb.draw(self.screen)
        self.player.sprite.fire_ball.draw(self.screen)
        self.building.draw(self.screen)
        self.bg_trees.draw(self.screen)
        self.bad_tower.draw(self.screen)
        self.enemy.draw(self.screen)
        self.bomb_exploded.draw(self.screen)
        self.grass.draw(self.screen)
        self.sparks.draw(self.screen)

        # Methods
        self.collisions()
        self.grass_position_checker()
        manual_menu.score = self.score

class Intro:
    def __init__(self,screen):
        self.screen = screen
        # self.game_stage = game_stage
        #Left Dog image
        self.left_dog = pygame.sprite.GroupSingle()
        self.left_dog.add(LeftDog())
        #Right Dog image
        self.right_dog = pygame.sprite.GroupSingle()
        self.right_dog.add(RightDog())
        #Top Dog image
        self.big_dog = pygame.sprite.GroupSingle()
        #Font
        self.font_small = pygame.font.Font('fonts/Amatic-Bold.ttf', 35)
        self.font = pygame.font.Font('fonts/Amatic-Bold.ttf', 50)
        self.font_big = pygame.font.Font('fonts/Amatic-Bold.ttf', 120)
        #Time Delay
        self.delay = 3500

    def display_with_delay(self):
        time = pygame.time.get_ticks()
        if time > self.delay:
            self.big_dog.add(BigDog())
            game_name_surf = self.font_big.render("Venom's Adventure", True,(0,0,102))
            message_surf = self.font.render('Press Space to continue',True, (0,0,102))
            instructions_surf = self.font_small.render('[arrows] to navigate                [space] to drop bombs', True, (0,0,102))
            game_name_rect = game_name_surf.get_rect(center = (640,550))
            message_rect = message_surf.get_rect(center = (640,650))
            instructions_rect = instructions_surf.get_rect(center = (640,700))
            self.screen.blit(game_name_surf,game_name_rect)
            self.screen.blit(message_surf,message_rect)
            self.screen.blit(instructions_surf,instructions_rect)
            self.big_dog.draw(self.screen)

    def run(self):
        # background setup
        self.screen.fill((153, 255, 255))
        self.left_dog.draw(self.screen)
        self.right_dog.draw(self.screen)
        self.display_with_delay()
        # self.get_input()


class ManualMenu:
    def __init__(self,screen, score):
        self.screen = screen
        # self.game_stage = game_stage
        self.font = pygame.font.Font('fonts/Amatic-Bold.ttf', 50)
        self.font_big = pygame.font.Font('fonts/Amatic-Bold.ttf', 100)
        self.font_small = pygame.font.Font('fonts/Amatic-Bold.ttf', 40)
        # Sprites
        self.fire_sprite = pygame.sprite.GroupSingle()
        self.fire_sprite.add(ManualFireBall((980, 200)))
        self.enemy_sprite = pygame.sprite.GroupSingle()
        self.enemy_sprite.add(ManualEnemy(275,425))
        self.enemy_two = pygame.sprite.GroupSingle()
        self.enemy_two.add(ManualEnemyTwo(350,400))
        self.manual_friend = pygame.sprite.GroupSingle()
        self.manual_friend.add(ManualFriend(875,400))
        self.score = score

    def run(self):
        self.screen.fill((153, 255, 255))
        # Dog image
        self.manual_surf = pygame.image.load('graphics/venom_manual_200_1.png').convert_alpha()
        self.manual_rect = self.manual_surf.get_rect(midbottom = (1150,810))
        self.screen.blit(self.manual_surf, self.manual_rect)
        # Bomb manual
        self.bomb_surf = pygame.image.load('graphics/bomb_32x32.png').convert_alpha()
        self.bomb_rect = self.bomb_surf.get_rect(midbottom = (300,200))
        self.screen.blit(self.bomb_surf,self.bomb_rect)

        # Enemies manual
        self.bad_tower_surf = pygame.image.load('graphics/bad_guys_tower.png').convert_alpha()
        self.bad_tower_surf = pygame.transform.rotozoom(self.bad_tower_surf, 0, 0.5)
        self.bad_tower_rect = self.bad_tower_surf.get_rect(midbottom=(500, 450))
        self.screen.blit(self.bad_tower_surf, self.bad_tower_rect)

        # Manual text
        self.bomb_text_surf = self.font.render('[SPACE] to drop', True, (0,0,102) )
        self.bomb_text_rect = self.bomb_text_surf.get_rect(midbottom = (300,250))
        self.screen.blit(self.bomb_text_surf, self.bomb_text_rect)

        self.fire_text_surf = self.font.render('[LEFT CTRL] to fire', True, (0, 0, 102))
        self.fire_text_rect = self.fire_text_surf.get_rect(midbottom = (1000,250))
        self.screen.blit(self.fire_text_surf, self.fire_text_rect)

        self.enemies_text_surf = self.font.render('enemies', True, (0, 0, 102))
        self.enemies_text_rect = self.enemies_text_surf.get_rect(midbottom = (400,500))
        self.screen.blit(self.enemies_text_surf,self.enemies_text_rect)

        self.friends_text_surf = self.font.render("friends (but shoot'em)", True, (0, 0, 102))
        self.friends_text_rect = self.friends_text_surf.get_rect(midbottom = (875, 500))
        self.screen.blit(self.friends_text_surf, self.friends_text_rect)

        self.manual_text_surf = self.font.render('[ARROW KEYS] to move', True, (0, 0, 102))
        self.manual_text_rect = self.manual_text_surf.get_rect(midbottom = (640,600))
        self.screen.blit(self.manual_text_surf, self.manual_text_rect)

        self.manual_text_surf_two = self.font.render('Watch out for people in buildings!', True, (0, 0, 102))
        self.manual_text_rect_two = self.manual_text_surf_two.get_rect(midbottom = (640,700))
        self.screen.blit(self.manual_text_surf_two, self.manual_text_rect_two)

        self.score_text_surf = self.font_big.render(f'Score: {self.score}', True, (0, 0, 102))
        self.score_text_rect = self.score_text_surf.get_rect(midbottom = (640,200))
        self.screen.blit(self.score_text_surf, self.score_text_rect)

        self.press_text_surf = self.font_small.render('press [SPACE] to play', True, (0, 0, 102))
        self.press_text_rect = self.press_text_surf.get_rect(midbottom = (640, 755))
        self.screen.blit(self.press_text_surf, self.press_text_rect)

        # Fire, enemies sprites manual
        self.fire_sprite.update()
        self.fire_sprite.draw(self.screen)
        self.enemy_sprite.update()
        self.enemy_sprite.draw(self.screen)
        self.enemy_two.update()
        self.enemy_two.draw(self.screen)
        self.manual_friend.update()
        self.manual_friend.draw(self.screen)


class GameState():
    def __init__(self):
        self.state = 'intro'

    def game(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == tree_setup:
                game.trees()
            if event.type == power_tower_setup:
                game.power_tower_setup()
            if event.type == building_setup:
                game.building_setup()
            if event.type == bad_tower:
                game.bad_guys_tower()
            if event.type == enemy:
                game.enemy_setup()
        game.run()
        if game.lives < 0:
            self.state = 'manual'
        pygame.display.flip()

    def intro(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        intro.run()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.state = 'game'
        pygame.display.flip()

    def manual(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        manual_menu.run()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            print('get input')
            self.state = 'game'
            game.lives = 3
            game.score = 0
        pygame.display.flip()

    def state_manager(self):
        if self.state == 'intro':
            self.intro()
        if self.state == 'game':
            self.game()
        if self.state == 'manual':
            self.manual()

if __name__ == '__main__':
    pygame.init()
    screen_width = 1280
    screen_height = 800
    screen = pygame.display.set_mode((screen_width,screen_height))
    pygame.display.set_caption("Venom's Adventures")
    icon = pygame.image.load('graphics/paws.png').convert_alpha()
    pygame.display.set_icon(icon)
    clock = pygame.time.Clock()
    # game_stage = 1
    score = 0
    game = Game(screen, score)
    intro = Intro(screen)
    manual_menu = ManualMenu(screen, score)
    game_state = GameState()
    # Time Triggers
    # Trees time trigger
    tree_setup = pygame.USEREVENT + 1
    pygame.time.set_timer(tree_setup,3000)
    # Power Tower time trigger
    power_tower_setup = pygame.USEREVENT + 2
    pygame.time.set_timer(power_tower_setup,4000)
    # Building trigger
    building_setup = pygame.USEREVENT + 3
    pygame.time.set_timer(building_setup,7000)
    # Bad Guys tower trigger
    bad_tower = pygame.USEREVENT + 4
    pygame.time.set_timer(bad_tower, 8000)
    # Enemies trigger
    enemy = pygame.USEREVENT + 5
    pygame.time.set_timer(enemy,5000)

    while True:
        game_state.state_manager()
        clock.tick(60)