import pygame as pg
import sys

from scripts.settings import *
from scripts.scenes.menu import Menu
from scripts.scenes.gameplay import GamePlay
from scripts.scenes.gameover import GameOver

class Game:

    def __init__(self):

        pg.init()
        pg.mixer.init()
        pg.font.init()
        pg.display.set_caption(NAME)
        
        self.display = pg.display.set_mode([WIDTH, HEIGHT])
        self.scene = "menu"
        self.current_scene = Menu()

        self.fps = pg.time.Clock()
    
    def run(self):
        
        while True:

            if self.scene == "menu" and self.current_scene.active == False:
                self.scene = "game"
                self.current_scene = GamePlay()
            elif self.scene == "game" and self.current_scene.active == False:
                self.scene = "gameover"
                self.current_scene = GameOver()
            elif self.scene == "gameover" and self.current_scene.active == False:
                self.scene = "menu"
                self.current_scene = Menu()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                    
                self.current_scene.events(event)
            
            self.fps.tick(60)
            self.display.fill([12, 159, 255])
            self.current_scene.draw()
            self.current_scene.update()
            pg.display.flip()