import pygame
import random
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, SCREEN_WIDTH

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, image_list, obstacle_type):
        super().__init__()
        self.image = random.choice(image_list)
        self.rect = self.image.get_rect()
        self.type = obstacle_type
        
        if self.type == 'small_cactus':
            self.rect.y = 325
        else:
            self.rect.y = 300
            
        self.rect.x = SCREEN_WIDTH
    def update(self, game_speed, obstacles):
        self.rect.x -= game_speed
        
        if self.rect.right < 0:
            obstacles.remove(self)
        