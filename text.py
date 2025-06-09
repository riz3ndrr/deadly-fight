import pygame as pyg

BLACK = (0, 0, 0)

class Text():
    def __init__(self, screen, font, color, text, coords):
        self.screen = screen
        self.x, self.y = coords
        self.render = font.render(text, True, color)
        self.shadow = font.render(text, True, BLACK)
    
    def draw(self):
        self.screen.blit(self.shadow, (self.x + 5, self.y + 5))
        self.screen.blit(self.render, (self.x, self.y))
        
    
    