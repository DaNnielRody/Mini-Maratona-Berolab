import pygame
import random
from dino_runner.utils.constants import CLOUD, SCREEN_WIDTH


class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.image = CLOUD
        
        self.image = pygame.transform.scale(
            self.image, (random.randint(80, 120), random.randint(40, 60)) # Isso dá as nuvens tamanhos aleatórios 
        )
        
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH + random.randint(200, 500)
        self.rect.y = random.randint(50, 150)
        
    def update(self, game_speed): # A nuvem irá se mover a cada instante do jogo, conforme a vel.
        self.rect.x -= game_speed
        
        if self.rect.right < 0:
            self.rect.x = SCREEN_WIDTH + random.randint(200, 500) # Os valores se resumem na aleatoriedade das aparições das nuvens.
            
            self.rect.y = random.randint(50, 150)
        