import pygame
import random 

from dino_runner.utils.constants import BIRD, SCREEN_WIDTH


class Bird(pygame.sprite.Sprite):
    
    BIRD_WIDTH = 80
    BIRD_HEIGHT = 60
    
    def __init__(self):
        super().__init__()
        
        self.image_list = [
             pygame.transform.scale(img, (self.BIRD_WIDTH, self.BIRD_HEIGHT))
             for img in BIRD
        ]
        
        
        self.image = self.image_list[0]
        self.step_index = 0
        
        self.rect = self.image.get_rect()
        
        self.rect.x = SCREEN_WIDTH + random.randint(200, 500)
        self.rect.y = random.randint(250, 290)
        
        self.fly_speed = 2
        
        self.fly_direction = 1  
        self.fly_timer = 0
        self.time_to_switch_direction = random.randint(40, 80) # Tempo para voar em uma direção

    def update(self, game_speed, obstacles):
        
        self.image = self.image_list[self.step_index // 5]
        self.step_index += 1
        
        if self.step_index >= 10:
            self.step_index = 0

        # --- Movimento "simples" ---
        self.rect.y += self.fly_direction * 1 # Move 1 pixel para cima ou para baixo
        self.fly_timer += 1
        if self.fly_timer > self.time_to_switch_direction:
            self.fly_direction *= -1 # Inverte a direção
            self.fly_timer = 0
        
        self.rect.x -= (game_speed + self.fly_speed)
        
        if self.rect.right < 0:
           obstacles.remove(self)