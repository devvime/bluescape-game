from scripts.scenes import scenes

class SceneManager:
    
    def __init__(self):
        self.scene = None
        self.current_scene = None
        
    def set_scene(self, scene):
        self.scene = scene
        self.current_scene = scenes[scene](self)
        
    def get_current_scene(self):
        return self.current_scene
        