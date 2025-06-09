import pygame as pyg

def attack1(self):
        """Primary attack"""
        self.attack_cooldown = 30
        if self.transformed is False:
            attacking_rect = pyg.Rect(self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y, 2 * self.rect.width, self.rect.height)
            #pyg.draw.rect(self.surface, (0, 255, 0), attacking_rect)

            if attacking_rect.colliderect(self.target.rect):
                if self.target.blocking is True:
                    self.target.health -= 10
                    self.target.glide_counter = 19
                else:
                    self.target.health -= 17
                    self.target.glide_counter = 18
                    self.target.hit = True
        else:
            if self.health + 7 > 100:
                self.health = 100
            else:
                self.health += 7

def attack2(self):
    global CRASH_DMG
    self.attack_cooldown = 10
    """Heavy attack"""
    if self.transformed == True:
        self.misc_attacking = True
        self.glide_counter = 0
        self.attacking_glide = True
        CRASH_DMG = 45
        self.vel_y = -30
    else:
        self.attack_cooldown = 5
        self.glide_counter = 13
        self.attacking_glide = True

        self.misc_attacking = True
        self.transformed = True
        CRASH_DMG = 20

    # if attacking_rect.colliderect(self.target.rect):
    #     if self.target.blocking is True:
    #         self.target.health -= 30
    #         self.target.glide_counter = 12
    #     else:
    #         self.target.health -= 39
    #         self.target.glide_counter = 7
        
    #         self.target.hit = True

def attack3(self):
    """sdfds"""
    self.attack_cooldown = 5
    if self.hit is True:
        self.transformed = False
    
    if self.transformed is True:
        self.transformed = False
    else:
        self.transformed = True
        
    
    
def misc_attack(self):
    global CRASH_DMG
    if self.hit is True:
        self.transformed = False
        self.misc_attacking = False
        self.glide_counter = 20
    if self.glide_counter < 20:
        attacking_rect = pyg.Rect(self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y, 2.5 * self.rect.width, self.rect.height)
        # pyg.draw.rect(self.surface, (0, 255, 0), attacking_rect)
        if attacking_rect.colliderect(self.target.rect):
            if self.target.blocking is True:
                self.target.health -= CRASH_DMG * 0.6
                self.target.glide_counter = 12
            else:
                self.target.health -= CRASH_DMG
                self.target.glide_counter = 7
                self.target.hit = True
            self.transformed = False
            self.misc_attacking = False
            self.glide_counter = 20
    else:
        self.misc_attacking = False
        self.transformed = False
        self.glide_counter = 20