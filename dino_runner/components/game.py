import pygame 
import sys 
import random
from dino_runner.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH, BG,SMALL_CACTUS, LARGE_CACTUS
from dino_runner.components.player import Player
from dino_runner.components.cloud import Cloud
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.components.obstacles.bird import Bird



class Game: 
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Chrome Dino Runner")
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.jogando = True

        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 380

        self.all_sprites = pygame.sprite.Group()
        self.cloud_group = pygame.sprite.Group()
        self.obstacle_group = pygame.sprite.Group()
        
        self.player = Player()
        self.all_sprites.add(self.player)
        
        for _ in range(5):
            cloud = Cloud()
            self.cloud_group.add(cloud)
            self.all_sprites.add(cloud)
        
        
    def execute (self):
        while self.jogando: 
            
            user_input = pygame.key.get_pressed()
            self.handle_events() # Verificar o que o jogador está fazendo
            self.update(user_input) # Mudança de estados
            self.draw()

            pygame.display.update()
            self.clock.tick(60)
            
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.shoot()

    def update(self, user_input):
        
        self.player.update(user_input)
        
        self.cloud_group.update(self.game_speed)
        
        self.update_background()
        self.spawn_obstacles()
        self.obstacle_group.update(self.game_speed, self.obstacle_group)
        self.check_collision()
        
        
    def spawn_obstacles(self):
        if len(self.obstacle_group) == 0:
            obstacle_type_choice = random.randint(0, 2)
            if obstacle_type_choice == 0:
                obstacle = Obstacle(SMALL_CACTUS, 'small_cactus')
            elif obstacle_type_choice == 1:
                obstacle = Obstacle(LARGE_CACTUS, 'large_cactus')
            else:
                obstacle = Bird()
            self.obstacle_group.add(obstacle)
            self.all_sprites.add(obstacle)
            
            
    def check_collision(self):
        if pygame.sprite.spritecollide(self.player, self.obstacle_group, False, pygame.sprite.collide_mask):
            self.player.die()
            self.draw()
            pygame.display.update()
            pygame.time.delay(2000)
            
            self.jogando = False
        
    def draw_background(self):
        image_width = BG.get_width()
        
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))    
    
    
    
    def update_background(self):
        image_width = BG.get_width()
        self.x_pos_bg -= self.game_speed
        
        if self.x_pos_bg <= -image_width:
            self.x_pos_bg = 0    
    
    
    def draw(self):
        self.screen.fill((0, 0, 0))
        self.draw_background()
        
        self.all_sprites.draw(self.screen) 
        for laser in self.player.lasers: # Adiciona o desenho dos lasers na tela
            pygame.draw.rect(self.screen, self.player.laser_color, laser)

        