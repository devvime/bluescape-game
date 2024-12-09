import pygame as pg
import sys

from scripts.settings import *
from scripts.components.scene_manager import SceneManager

class Game:

    def __init__(self):

        pg.init()
        pg.mixer.init()
        pg.font.init()
        pg.display.set_caption(NAME)
        
        self.display = pg.display.set_mode([WIDTH, HEIGHT])
        
        self.scene_manager = SceneManager()
        self.scene_manager.set_scene("menu")

        self.fps = pg.time.Clock()
    
    def run(self):
        
        while True:

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                    
                if self.scene_manager.current_scene:
                    self.scene_manager.current_scene.events(event)
            
            self.fps.tick(60)
            self.display.fill([12, 159, 255])
            
            if self.scene_manager.current_scene:
                self.scene_manager.current_scene.draw()
                self.scene_manager.current_scene.update()
            
            pg.display.flip()