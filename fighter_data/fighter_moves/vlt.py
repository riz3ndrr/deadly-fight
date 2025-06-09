import pygame as pyg

def attack1(self):
        """Primary attack"""
        self.attack_cooldown = 0
        attacking_rect = pyg.Rect(self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y, 3 * self.rect.width, self.rect.height)
        # pyg.draw.rect(self.surface, (0, 255, 0), attacking_rect)

        if attacking_rect.colliderect(self.target.rect):
            if self.target.blocking is True:
                self.target.health -= 11
                self.target.glide_counter = 19
                self.target.meter -= 30
            else:
                self.target.health -= 7
                self.target.glide_counter = 19
                self.target.hit = True
                self.target.meter -= 40


def attack2(self):
    self.attack_cooldown = 50
    """Heavy attack"""
    if self.projectile_fired is False:
        self.projectile_fired = True

        self.projectile_img = pyg.image.load("assets/images/misc/lightning.png").convert_alpha()
        self.projectile_scale = (200, 100)
        self.projectile_img = pyg.transform.scale(self.projectile_img, self.projectile_scale)
        
        self.projectile_dmg = 13
        if self.flip is True:
            self.projectile_rect = self.projectile_img.get_rect(center = [self.rect.x - 50, self.rect.y+50])
            self.projecitle_flipped = True
            self.projectile_speed = -17
        else:
            self.projectile_rect = self.projectile_img.get_rect(center = [self.rect.x+170, self.rect.y+50])
            self.projecitle_flipped = False
            self.projectile_speed = 17
        
        

        

def attack3(self):
    """sdfds"""
    self.meter += 5
    self.health -= 1.5
    
