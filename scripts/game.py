import pygame
from scripts.fade import Fade
from scripts.obj import Obj
from scripts.settings import *
from scripts.map import *
from scripts.player import Player
from scripts.camera import Camera

class Game:

    def __init__(self):
        
        self.display = pygame.display.get_surface()
        self.all_sprites = Camera()
        self.enemy_colision = pygame.sprite.Group()
        self.all_colision = pygame.sprite.Group()
        self.active = True
        self.fade = Fade(5)
        self.tick = 0
        
        self.generate_map()
        self.player = Player(pos=(0, 0), groups=[self.all_sprites], collision_group=self.all_colision)

        #self.music = pygame.mixer.Sound("file")
        #self.music.play(-1)
        
    def generate_map(self):
        for row_index, row in enumerate(map1):
            for col_index, col in enumerate(row):
                x = col_index * map1_tile_size
                y = row_index * map1_tile_size
                
                if col == "x":
                    Obj("assets/tile/tile.png", [x, y], [self.all_sprites, self.all_colision])

    def colision(self):
        pass

    def gameover(self):
        pass
    
    def events(self, event):
        pass
    
    def draw(self):
        self.all_sprites.render(self.player)
                
    def update(self):
        self.fade.draw()
        self.all_sprites.update()
        self.colision()
        self.gameover()
