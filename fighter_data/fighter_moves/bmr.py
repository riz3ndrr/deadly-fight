import pygame as pyg

def attack1(self):
        """Primary attack"""
        self.attack_cooldown = 30
        attacking_rect = pyg.Rect(self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y, 2 * self.rect.width, self.rect.height)
        # pyg.draw.rect(self.surface, (0, 255, 0), attacking_rect)

        if attacking_rect.colliderect(self.target.rect):
            if self.target.blocking is True:
                self.target.health -= 5
                self.target.glide_counter = 19
            else:
                self.target.health -= 10
                self.target.glide_counter = 18
                self.target.hit = True

def attack2(self):
    self.attack_cooldown = 50
    """Heavy attack"""
    attacking_rect = pyg.Rect(self.rect.centerx - 3 * self.rect.width, self.rect.y - 150, 7 * self.rect.width, self.rect.height * 2)
    # pyg.draw.rect(self.surface, (0, 255, 0), attacking_rect)
    self.health -= 30
    if attacking_rect.colliderect(self.target.rect):
        if self.target.blocking is True:
            self.target.health -= 30
            self.target.glide_counter = 12
        else:
            self.target.health -= 55
            self.target.glide_counter = 7
        
            self.target.hit = True

def attack3(self):
    """sdfds"""
    """ CHANGE THINGS TO SELF.PROJECTILE.VEL_Y ETCC"""
    self.misc_attacking = True
    self.attack_cooldown = 40
    self.projectile_scale = (64, 64)
    self.projectile_dmg = 18

    self.projectile_vel_y = 0
    self.projectile_dy = -60

    self.projectile_img = pyg.image.load("assets/images/misc/bomb.png").convert_alpha()
    self.projectile_img = pyg.transform.scale(self.projectile_img, self.projectile_scale)

    if self.flip is True:
        self.projectile_rect = self.projectile_img.get_rect(center = [self.rect.x, self.rect.y+50])
        self.projecitle_flipped = True
        self.projectile_speed = -20
    else:
        self.projectile_rect = self.projectile_img.get_rect(center = [self.rect.x+170, self.rect.y+50])
        self.projecitle_flipped = False
        self.projectile_speed = 20

def misc_attack(self, screen_width):
    """sfds"""
    if self.projectile_rect.colliderect(self.target.rect):
        # if bomb hits opponent
        self.misc_attacking = False
        # Resets 
        #self.projectile_rect = self.projectile.get_rect(center = [self.rect.x+230, self.rect.y+50])
        # Damage
        if self.target.blocking is True:
            self.target.health -= self.projectile_dmg * 0.3
        else:
            self.target.health -= self.projectile_dmg
            self.target.hit = True
    
    # If bomb goes offscreen
    if self.projectile_rect.left  + self.projectile_speed  < 0:
        self.projectile_speed = -self.projectile_rect.left
        self.projectile_rect.x += self.projectile_speed
        
    elif self.projectile_rect.right + self.projectile_speed > 1000:
        self.projectile_speed = 1000 - self.projectile_rect.right
        self.projectile_rect.x += self.projectile_speed
    
    if self.projectile_rect.y + self.projectile_dy > 490:
        self.projectile_dy = 0
        
    # movement
    else:
        self.projectile_vel_y += 1
        self.projectile_dy += self.projectile_vel_y

        if self.projectile_flipped is True:
            # Changes direction of sprite depending on player direction
            self.projectile_rect.x += -self.projectile_speed
            self.projectile_img = pyg.transform.rotate(self.projectile_img, 180)
        
        else:
            self.projectile_rect.x += self.projectile_speed
        
    self.projectile_rect.y += self.projectile_dy
    # Draws sprite
    self.surface.blit(self.projectile_img, self.projectile_rect)

