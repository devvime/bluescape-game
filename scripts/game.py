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
        self.screen_info = pg.display.Info()
        self.virtual_screen = pg.Surface((self.screen_info.current_w, self.screen_info.current_h))
        self.scaled_screen = pg.transform.scale(self.virtual_screen, [self.screen_info.current_w, self.screen_info.current_h])
        self.fullscreen = False
        
        self.scene_manager = SceneManager(display=self.virtual_screen)
        self.scene_manager.set_scene("menu")

        self.fps = pg.time.Clock()
    
    def run(self):
        
        while True:

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.fullscreen = False
                    pg.quit()
                    sys.exit()
                    
                if event.type == pg.VIDEORESIZE:
                    self.screen_info = pg.display.Info()
                    
                if self.scene_manager.current_scene:
                    self.scene_manager.current_scene.events(event)
            
            self.fps.tick(FPS)
            self.virtual_screen.fill([12, 159, 255])
            
            if self.scene_manager.current_scene:
                self.scene_manager.current_scene.draw()
                self.scene_manager.current_scene.update()
                
            self.scaled_screen = pg.transform.scale(self.virtual_screen, [self.screen_info.current_w, self.screen_info.current_h])
            self.display.blit(self.scaled_screen, [0, 0])
                        
            pg.display.flip()
            pg.display.update()
            
            if FULLSCREEN and not self.fullscreen:
                self.display = pg.display.set_mode([WIDTH, HEIGHT], pg.FULLSCREEN)
                self.screen_info = pg.display.Info()
                self.fullscreen = True