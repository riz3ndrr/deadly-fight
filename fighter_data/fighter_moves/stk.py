import pygame as pyg

def attack1(self):
        """Primary attack"""
        DMG = 10
        self.attack_cooldown = 20
        if self.transformed:
            DMG = 12
            self.attack_cooldown = 14

        
        attacking_rect = pyg.Rect(self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y, 2 * self.rect.width, self.rect.height)
        # pyg.draw.rect(self.surface, (0, 255, 0), attacking_rect)
        if attacking_rect.colliderect(self.target.rect):
            if self.target.blocking is True:
                self.target.health -= DMG * 0.5
                self.target.glide_counter = 19
            else:
                self.target.health -= DMG
                self.target.hit = True
                self.target.glide_counter = 18
        

def attack2(self):
        """Heavy attack"""
        self.attack_cooldown = 35
        
        if self.transformed is False:
            # Normal Heavy Attack
            DMG = 30
            attacking_rect = pyg.Rect(self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y, 2 * self.rect.width, self.rect.height)
            # pyg.draw.rect(self.surface, (0, 255, 0), attacking_rect)
            if attacking_rect.colliderect(self.target.rect):
                if self.target.blocking is True:
                    self.target.health -= DMG * 0.5
                    self.target.glide_counter = 16
                else:
                    self.target.health -= DMG
                    self.target.glide_counter = 7
                
                    self.target.hit = True
        else:
        # Transformed Heavy Attack / Teleport
            key = pyg.key.get_pressed()
            if key[pyg.K_s] and self.player == 1 or key[pyg.K_DOWN] and self.player == 2:
                # keep-away teleport
                if self.flip:
                    # When player is on the right side of the screen
                    self.rect.x = 900
                else:
                    # When player is on the left side of the screen 
                    self.rect.x = 0
            else:
                # charging teleport
                if self.flip:
                    # When player is on the right side of the screen
                    self.rect.x = self.target.rect.x + 150
                else:
                    # When player is on the left side of the screen 
                    self.rect.x = self.target.rect.x - 150

def attack3(self):
    if self.transformed is False:
        self.transformed = True
        self.health += 25
        self.name = 'The Stick Avatar'
        self.attack_cooldown = 100
    else:
        if self.projectile_fired is False:
            self.projectile_fired = True
            self.projectile_img = pyg.image.load('assets/images/misc/purple-projectile.png').convert_alpha()
            self.projectile_rect = self.projectile_img.get_rect(center = [self.rect.x, self.rect.y+50])

            if self.flip:
                self.projectile_flipped = True
            else:
                self.projectile_flipped = False