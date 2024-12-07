import random
import pygame
from scripts.animatedbg import AnimatedBg
from scripts.obj import Obj
from scripts.scene import Scene
from scripts.settings import *
from scripts.text import Text
from scripts.map import *
from scripts.player import Player

class Game(Scene):

    def __init__(self):
        super().__init__()

        self.tick = 0
        self.enemy_colision = pygame.sprite.Group()
        self.all_colision = pygame.sprite.Group()
        
        self.generate_map()

        #self.music = pygame.mixer.Sound("file")
        #self.music.play(-1)
        
    def generate_map(self):
        for row_index, row in enumerate(map1):
            for col_index, col in enumerate(row):
                x = col_index * map1_tile_size
                y = row_index * map1_tile_size
                
                if col == "x":
                    Obj("assets/tile/tile.png", [x, y], [self.all_sprites])
                elif col == "p":
                    Player(pos=(x, y), groups=[self.all_sprites])

    def colision(self):
        pass

    def gameover(self):
        pass
                
    def update(self):
        self.colision()
        self.gameover()
        return super().update()
