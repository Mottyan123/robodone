# title: test
# author: Kazunori Hashimoto
# site: https://github.com/Mottyan123/robodan
# license: MIT

import pyxel

class App:
    def __init__(self): 
        pyxel.init(160, 256, title="test") 
        self.char_x = 50
        self.char_y = 60
        self.gravity = 0.0
        self.jump1 = False
        self.jump2 = False
        self.score = 0 
        pyxel.run(self.update, self.draw) 

    def update(self): 
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and not self.jump1 and not self.jump2:
            self.gravity = 9
        
        if pyxel.btnr(pyxel.MOUSE_BUTTON_LEFT):
            self.jump1 = True
    
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and self.jump1 and not self.jump2:
            self.gravity = 9
            self.jump2 = True
            
        self.gravity -= 0.9
        self.char_x += self.gravity
        
        if self.char_x < 50:
            self.char_x = 50
            self.jump1 = False
            self.jump2 = False
            self.gravity = 0.0

    def draw(self): 
        pyxel.cls(6)
        pyxel.rect(self.char_x, self.char_y, 8, 8, 9)

App()