import pygame as pyg

class Button():
    def __init__(self, x, y, screen, rotated_up, image, size):
        self.image = pyg.transform.scale(pyg.image.load(image), size)
        if rotated_up:
            self.image = pyg.transform.flip(self.image,  False, True)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.screen = screen
        self.clicked = False
    
    
    def draw(self):
        action = False
        pos = pyg.mouse.get_pos()
        
        if self.rect.collidepoint(pos):
            if pyg.mouse.get_pressed()[0] is True and self.clicked is False:
                self.clicked = True
                action = True
            if pyg.mouse.get_pressed()[0] is False and self.clicked is True:
                self.clicked = False
        self.screen.blit(self.image, (self.rect.x, self.rect.y))
        return action