import pygame 
from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING, DUCKING_SHIELD, ICON, DEAD


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.dino_run = RUNNING 
        self.dino_jump = JUMPING
        self.dino_duck = DUCKING
        self.dino_dead = DEAD
        
        self.step_index = 0
        
        # Imagem digital e retângulo de colisão
        self.image = self.dino_run[0]
        self.rect = self.image.get_rect()
        self.rect.x = 80
        self.rect.y = 310

        self.is_running = True
        self.is_jumping = False
        self.is_ducking = False
        
        self.jump_vel = 7
        
        #lasers
        self.lasers = []
        self.laser_speed = 15 
        self.laser_color = (255, 0, 0)
        self.max_lasers = 100
    
    def run (self):
        self.image = self.dino_run[self.step_index // 5]
        
        self.rect.y = 310
        self.step_index += 1
        
        if self.step_index >= 10:
            self.step_index = 0
    
    def jump (self):
        self.image = self.dino_jump
        
        self.rect.y -= self.jump_vel * 4
        self.jump_vel -= 0.4
        
        if self.jump_vel < -7:
            self.is_jumping = False
            self.jump_vel = 7

    def duck (self):
        self.image = self.dino_duck[self.step_index // 5]
        
        self.rect.y = 340
        self.step_index += 1
        
        if self.step_index >= 10:
            self.step_index = 0
    
    
    def shoot (self):
        if len(self.lasers) < self.max_lasers:
            laser_rect = pygame.Rect(self.rect.right, self.rect.centery - 2, 20, 4)
            self.lasers.append(laser_rect)
            
    def die(self):
        self.image = self.dino_dead
        self.rect.y = 310
    
    
    def update (self, user_input):
        
        if user_input [pygame.K_UP] and not self.is_jumping:
            self.is_running = False
            self.is_jumping = True
            self.is_ducking = False
        elif user_input [pygame.K_DOWN] and not self.is_jumping:
            self.is_running = False
            self.is_jumping = False
            self.is_ducking = True
        elif not (self.is_jumping  or user_input[pygame.K_DOWN]):
            self.is_running = True
            self.is_jumping = False
            self.is_ducking = False
        
            
        if self.is_running:
            self.run()
        elif self.is_jumping:
            self.jump()
        elif self.is_ducking:
            self.duck()
          
        
        for laser in self.lasers:
            laser.x += self.laser_speed
            
            
        self.lasers = [laser for laser in self.lasers if laser.x < 1200]
        
    
