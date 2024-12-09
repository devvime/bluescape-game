import pygame as pg

from scripts.settings import *
from scripts.data.map import *
from scripts.components.fade import Fade
from scripts.components.entity import Entity
from scripts.entities.player import Player
from scripts.components.camera import Camera
from scripts.entities.ui import Ui

class GamePlay:

    def __init__(self, scene_manager):
        
        self.scene_manager = scene_manager        
        self.display = pg.display.get_surface()
        self.all_sprites = Camera()
        self.enemy_colision = pg.sprite.Group()
        self.all_colision = pg.sprite.Group()
        self.active = True
        self.fade = Fade(speed=5)
        self.tick = 0
        
        self.finish = Entity("assets/tile/finish.png", [0, 0], [self.all_sprites])
        self.player = Player(pos=(0, 0), groups=[self.all_sprites], collision_group=self.all_colision)
        self.hud_ui = Ui()
        
        self.generate_map()
        

        #self.music = pg.mixer.Sound("file")
        #self.music.play(-1)
        
    def generate_map(self):
        for row_index, row in enumerate(map1):
            for col_index, col in enumerate(row):
                x = col_index * map1_tile_size
                y = row_index * map1_tile_size
                
                if col == "x":
                    Entity("assets/tile/tile.png", [x, y], [self.all_sprites, self.all_colision])
                elif col == "c":
                    self.finish.rect.x = x
                    self.finish.rect.y = y

    def colision(self):
        if self.player.rect.colliderect(self.finish.rect):
            self.scene_manager.set_scene("gameover")

    def gameover(self):
        if self.player.rect.y > HEIGHT + 350:
            self.player.rect.x = 0
            self.player.rect.y = 0
            self.hud_ui.life -= 1
            
        if self.hud_ui.life <= 0:
            self.scene_manager.set_scene("gameover")
    
    def events(self, event):
        pass
    
    def draw(self):
        self.all_sprites.render(self.player)
        self.hud_ui.draw()
                
    def update(self):
        self.all_sprites.update()
        self.colision()
        self.gameover()
        self.hud_ui.update()
        self.fade.draw()
