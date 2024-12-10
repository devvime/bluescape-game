import pygame as pg

class Animator:
    def __init__(self):
        self.anims = {}
        self.tick = 0
    
    def create(self, name, path, frames, flip=False, speed=8):
        anim = {
            "frame": 0,
            "frames": [],
            "speed": speed,
            "tick": 0
        }
        for i in range(frames):
            try:
                image = pg.image.load(f"{path}_{i}.png").convert_alpha()
                if flip:
                    image = pg.transform.flip(image, True, False)
                anim["frames"].append(image)
            except FileNotFoundError:
                print(f"Error: File not found {path}_{i}.png")
                break
        
        self.anims[name] = anim

    def play(self, name):
        if name not in self.anims:
            print(f"Erro: Animation '{name}' not found.")
            return None
        
        anim = self.anims[name]
        anim["tick"] += 1
        if anim["tick"] >= anim["speed"]:
            anim["tick"] = 0
            anim["frame"] = (anim["frame"] + 1) % len(anim["frames"])
        
        return anim["frames"][anim["frame"]]
