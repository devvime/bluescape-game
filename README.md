# BlueScape Game with Pygame

Simple game developed with Pygame

### Scenes

Create your scenes in ``` scripts/scenes/ ```

Default scene:

```python
import pygame as pg
import sys

from scripts.settings import *
from scripts.components.scene import Scene

class MyScene(Scene):

    def __init__(self, scene_manager):
        super().__init__()
        
        self.scene_manager = scene_manager
    
    def events(self, event):
        # code here
        return super().events(event)

    def draw(self):
        # code here
        return super().draw()

    def update(self):
        # code here
        return super().update()
```

import your scenes in ``` scripts/scenes/__init__.py ```

__init__.py

```python
from scripts.scenes.menu import Menu
from scripts.scenes.gameplay import GamePlay
from scripts.scenes.gameover import GameOver
from scripts.scenes.my_scene import MyScene

scenes = {
    "menu": Menu,
    "gameplay": GamePlay,
    "gameover": GameOver,
    "my_scene": MyScene
}
```

Change scene

```python
self.scene_manager.set_scene("my_scene")
```
