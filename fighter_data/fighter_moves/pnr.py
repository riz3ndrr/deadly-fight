import pygame as pyg

def attack1(self):
        """Primary attack"""
        self.attack_cooldown = 3
        attacking_rect = pyg.Rect(self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y, 2 * self.rect.width, self.rect.height)
        # pyg.draw.rect(self.surface, (0, 255, 0), attacking_rect)

        if attacking_rect.colliderect(self.target.rect):
            if self.target.blocking is True:
                self.target.health -= 7
                self.target.glide_counter = 19
            else:
                self.target.health -= 12
                self.target.glide_counter = 18
                self.target.hit = True

def attack2(self):
    self.attack_cooldown = 50
    """Heavy attack"""
    attacking_rect = pyg.Rect(self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y, 3 * self.rect.width, self.rect.height)
    # pyg.draw.rect(self.surface, (0, 255, 0), attacking_rect)

    if attacking_rect.colliderect(self.target.rect):
        if self.target.blocking is True:
            self.target.health -= 30
            self.target.glide_counter = 12
        else:
            self.target.health -= 43
            self.target.glide_counter = 7
        
            self.target.hit = True

def attack3(self):
    """sdfds"""
    self.attack_cooldown = 5
    self.glide_counter = 6
    self.attacking_glide = True
    
