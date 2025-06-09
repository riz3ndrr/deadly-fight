import pygame as pyg
import fighter_data.fighter_moves.pnr as pnr
import fighter_data.fighter_moves.stk as stk
import fighter_data.fighter_moves.bmr as bmr
import fighter_data.fighter_moves.trn as trn
import fighter_data.fighter_moves.vlt as vlt



class Fighter():
    def __init__(self, x, y, player, flip, data, sprite_sheet):
        self.rect = pyg.Rect((x, y, 80, 180))
        self.player = player
        self.vel_y = 0
        self.jump = False
        self.attacking = False
        self.blocking = False
        self.hit = False
        self.data = data
        
        self.attack_type = 0
        self.attack_cooldown = 0
        self.misc_attacking = False

        self.health = 100
        self.meter = 100
        self.alive = True

        self.transformed = False
        self.can_transform = data[7]

        self.flip = flip
        # 0:idle 1:run 2:jump 3:hit 4:death 5:block 6:attack1 7:attack2 8:attack3
        self.action = 0
        self.frame_index = 0
        self.size = data[0]
        self.scale = data[1]
        self.offset = data[2]
        animation_steps = data[3]

        self.animation_list = self.load_images(sprite_sheet, animation_steps)
        self.animation_index = data[4]
        
        self.name = data[5]
        self.fighter_id = data[6]

        self.image = self.animation_list[self.frame_index]
        self.update_time = pyg.time.get_ticks()

        self.running = False

        # Gliding
        self.attacking_glide = False
        self.gliding = False
        self.glide_counter = 20

        # Projectile
        self.projectile_fired = False
        self.projectile_flipped = False
        self.projectile_speed = 20
        self.projectile_dy = -60
        self.projectile_vel_y = 0
        self.projectile_dmg = 20
        self.projectile_img = None
        self.projectile_rect = None
        self.projectile_scale = (100, 100)

    def update_meter(self):
        if self.meter < 0:
            self.meter = 0
        if self.meter > 100:
            self.meter = 100
        
        if self.meter < 100:
            if self.transformed:
                if self.fighter_id == 'STK':
                    self.meter += 0.55
                elif self.fighter_id == 'TRN':
                    self.meter += 0.1
            else:
                self.meter += 0.35

        
    

    

    def change_action(self, new_action):
        # Check if the new action is different to the previous one
        if new_action != self.action:
            self.action = new_action
            self.frame_index = 0
            self.update_time = pyg.time.get_ticks()

    
    # Handle animation updates
    def update(self):
        # Check what action the player is performing
        # 0:idle 1:run 2:jump 3:hit 4:death 5:block 6:attack1 7:attack2 8:attack3
        # When 'transformed'    
        # 9: idle, 10: run, 11:jump, 12:hit, 13:death, 14th:block, 15:attack1, 16:attack2, 17:attack3
        animation_cooldown = 170
        

        if self.health <= 0:
            self.health = 0
            self.alive = False
            action_index = 4

        elif self.hit:
            action_index = 3
            if self.fighter_id == 'TRN' and self.transformed:
                self.transformed = False
        
        elif self.attacking:
            animation_cooldown = 30
            
            if self.attack_type == 1:
                action_index = 6

            elif self.attack_type == 2:
                action_index = 7

            elif self.attack_type == 3:
                action_index = 8
        elif self.jump:
            action_index = 2

        elif self.running:
            action_index = 1

        elif self.blocking:
            action_index = 5            
        else:
            # Idle
            action_index = 0
        
        if self.transformed:
            # Difference between the position of normal and transformed
            # actions is 9
            action_index += 9
        self.change_action(action_index)
        

            
            


        
        # Update image
        self.image = self.animation_list[self.animation_index[self.action][self.frame_index]]

        # Check if enough time has passed since the last update
        if pyg.time.get_ticks() - self.update_time > animation_cooldown:
            self.frame_index += 1
            self.update_time = pyg.time.get_ticks()
        
        # Check if the animation has finished
        if self.frame_index >= len(self.animation_index[self.action]):

            if self.alive is False:
                self.frame_index = len(self.animation_index[self.action]) - 1
            else:
                self.frame_index = 0


            
            # if player was hit
            if self.action == 3 or self.action == 12:
                self.hit = False
                # if player was in the middle of an attack
                self.attacking = False
                self.attack_cooldown = 30

        

            # Check if an attack was executed / Attack animation has finished
            if self.action == 6 or self.action == 15:
                self.attacking = False
                # Make attack cooldown defined in the specific attack class
                
                self.attack1()

            elif self.action == 7 or self.action == 16:
                self.attacking = False
                
                self.attack2()
            
            elif self.action == 8 or self.action == 17:
                self.attacking = False
                self.attack3()
    
    def attack1(self):
        """Primary attack"""
        if self.fighter_id == 'PNR':
            pnr.attack1(self)
        elif self.fighter_id == 'STK':
            stk.attack1(self)
        elif self.fighter_id == 'BMR':
            bmr.attack1(self)
        elif self.fighter_id == 'TRN':
            trn.attack1(self)
        elif self.fighter_id == 'VLT':
            vlt.attack1(self)



    def attack2(self):  
        """Heavy attack"""
        if self.fighter_id == 'PNR':
            pnr.attack2(self)
        elif self.fighter_id == 'STK':
            stk.attack2(self)
        elif self.fighter_id == 'BMR':
            bmr.attack2(self)
        elif self.fighter_id == 'TRN':
            trn.attack2(self)
        elif self.fighter_id == 'VLT':
            vlt.attack2(self)
    
    def attack3(self):  
        """Misc attack
        All projectile attacks should be under attack3
        self.projectile.flipped to avoid switching direction bug"""
        if self.fighter_id == 'PNR':
            pnr.attack3(self)
        elif self.fighter_id == 'STK':
            stk.attack3(self)
        elif self.fighter_id == 'BMR':
            bmr.attack3(self)
        elif self.fighter_id == 'TRN':
            trn.attack3(self)
        elif self.fighter_id == 'VLT':
            vlt.attack3(self)
    

    def misc_attack(self, screen_width):
        """misc attack"""
        if self.misc_attacking:
            if self.fighter_id == 'PNR':
                pnr.misc_attack(self)
            elif self.fighter_id == 'STK':
                stk.misc_attack(self)
            elif self.fighter_id == 'BMR':
                bmr.misc_attack(self, screen_width)
            elif self.fighter_id == 'TRN':
                trn.misc_attack(self)
        
        



    def load_images(self, sprite_sheet, animation_steps):
        # Extract images from spritesheet
        animation_list = []
        for x in range(animation_steps):
            temp_img = sprite_sheet.subsurface(x * self.size , 0, self.size, self.size)
            
            animation_list.append(pyg.transform.scale(temp_img, (self.size * self.scale, self.size * self.scale)))
        return animation_list


    def reset(self, x, flip, data):
        """reset fighter variables"""
        self.rect.x = x
        self.flip = flip
        self.health = 100
        self.meter = 100
        self.name = data[5]
        self.alive = True
        self.hit = False
        self.transformed = False
        self.misc_attacking = False
    

    def update_projectile(self, surface, screen_width):
        """update projectile"""
        if self.projectile_fired:
            # Scales image
            self.projectile_img = pyg.transform.scale(self.projectile_img, self.projectile_scale)

            
            if self.projectile_flipped:
                self.projectile_rect.x -= self.projectile_speed
            else:
                self.projectile_rect.x += self.projectile_speed

            if self.projectile_rect.colliderect(self.target.rect):
                

                if self.target.blocking is True:
                    self.target.health -= self.projectile_dmg * 0.3
                    if self.fighter_id == 'VLT':
                        self.target.meter -= 35
                else:
                    if self.fighter_id == 'VLT':
                        self.target.meter -= 50
                    self.target.health -= self.projectile_dmg
                    self.target.hit = True
                self.projectile_fired = False

            # When projectile is about to go off screen
            if self.projectile_rect.left + self.projectile_speed < 0 or self.projectile_rect.right > screen_width:
                
                
                self.projectile_fired = False
            # Draws / blits the image
            surface.blit(self.projectile_img, self.projectile_rect)



            
            
            


    def move(self, screen_width, screen_height, surface, target, floor_height):
        SPEED = 10
        if self.transformed:
            SPEED = 13

        GRAVITY = 2
        dx = 0
        dy = 0
        self.surface = surface
        self.target = target
        self.running = False
        self.blocking = False
        

        
        # get keypresses
        key = pyg.key.get_pressed()


        # How much stamina each attack should take for each character:
        stamina_dict = {'PNR':[30, 50, 20],
                        'STK': [30, 50, 30],
                        'BMR': [30, 60, 40],
                        'TRN': [25, 50, 0],
                        'VLT': [20, 50, 0]}

        # Can only attack if doing nothing else 
        if self.attacking is False and self.alive is True and self.glide_counter == 20:


            # player 1 controls
            if self.player == 1 and self.hit is False:
                # Can't move when hit
                # movement
                if key[pyg.K_a]:
                    dx = -SPEED
                    self.running = True

                elif key[pyg.K_d]:
                    dx = SPEED
                    self.running = True

                elif key[pyg.K_f] and self.jump is False and self.transformed is False:
                    # Note: Transformed players can't block
                    self.blocking = True
                    self.meter -= 0.5


                if key[pyg.K_w] and self.jump is False and self.blocking is False:
                    self.vel_y = -40
                    self.jump = True
                    self.meter -= 35

                # Attack
                if key[pyg.K_e] or key[pyg.K_r] or key[pyg.K_t]:
                    if self.attack_cooldown == 0:
                        # Determine which attack type was used
                        
                        if key[pyg.K_e] and self.meter >= stamina_dict[self.fighter_id][0]:
                            self.attack_type = 1
                            self.meter -= 25
                            self.attacking = True
                            
                        elif key[pyg.K_r] and self.meter >= stamina_dict[self.fighter_id][1]:
                            self.attack_type = 2
                            self.meter -= 50
                            self.attacking = True

                        elif key[pyg.K_t] and self.meter >= stamina_dict[self.fighter_id][2]:
                            if self.fighter_id == 'STK':
                                if self.health <= 30 and self.transformed is False:
                                    self.meter -= stamina_dict[self.fighter_id][2]
                                    self.attacking = True
                                    self.attack_type = 3
                                elif self.transformed:
                                    self.meter -= stamina_dict[self.fighter_id][2]
                                    self.attacking = True
                                    self.attack_type = 3
                            else:
                                self.attack_type = 3
                                self.meter -= stamina_dict[self.fighter_id][2]
                                self.attacking = True
    

            elif self.player == 2 and self.hit is False:
                # Can't move when hit
                # movement
                if key[pyg.K_LEFT]:                     
                    dx = -SPEED
                    self.running = True

                elif key[pyg.K_RIGHT]:
                    dx = SPEED
                    self.running = True

                elif key[pyg.K_RSHIFT] and self.jump is False and self.transformed is False:
                    # Note: Transformed players can't block
                    self.meter -= 0.5
                    self.blocking = True


                if key[pyg.K_UP] and self.jump is False and self.blocking is False:
                    self.vel_y = -40
                    self.jump = True
                    self.meter -= 35

                # Attack
                if key[pyg.K_COMMA] or key[pyg.K_PERIOD] or key[pyg.K_SLASH]:
                    if self.attack_cooldown == 0:
                        # Determine which attack type was used
                        
                        if key[pyg.K_COMMA] and self.meter >= stamina_dict[self.fighter_id][0]:
                            self.attack_type = 1
                            self.meter -= 25
                            self.attacking = True
                            
                        elif key[pyg.K_PERIOD] and self.meter >= stamina_dict[self.fighter_id][1]:
                            self.attack_type = 2
                            self.meter -= 50
                            self.attacking = True

                        elif key[pyg.K_SLASH] and self.meter >= stamina_dict[self.fighter_id][2]:
                            if self.fighter_id == 'STK':
                                if self.health <= 30 and self.transformed is False:
                                    self.meter -= stamina_dict[self.fighter_id][2]
                                    self.attacking = True
                                    self.attack_type = 3
                                elif self.transformed:
                                    self.meter -= stamina_dict[self.fighter_id][2]
                                    self.attacking = True
                                    self.attack_type = 3
                            else:
                                self.attack_type = 3
                                self.meter -= stamina_dict[self.fighter_id][2]
                                self.attacking = True


        # Apply gravity
        self.vel_y += GRAVITY
        dy += self.vel_y

        
        # Ensures player stays on screen
        if self.rect.left + dx  < 0:
            dx = -self.rect.left
        if self.rect.right + dx > screen_width:
            dx = screen_width - self.rect.right
        if self.rect.bottom + dy > screen_height - floor_height:
            self.vel_y = 0 
            self.jump = False
            dy = screen_height - floor_height - self.rect.bottom
        
        
        
        # Ensure players face each other
        if target.rect.centerx > self.rect.centerx:
            self.flip = False
        else:
            self.flip = True

        # Apply attack cooldown
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1



        # update player position
        self.rect.x += dx
        self.rect.y += dy

         # Gliding
        glide_speed = 30
        if self.glide_counter != 20:
            # If the player is supposed to advance forward
            if self.attacking_glide:
                if self.flip:
                    self.rect.x -= glide_speed
                else:
                    self.rect.x -= -glide_speed
            else:
            # If the player is supposed to be pushed back
                if self.flip:
                    self.rect.x += glide_speed
                else:
                    self.rect.x += -glide_speed
            self.glide_counter += 1

        else:
            self.attacking_glide = False
            
    

    def draw(self, surface):
        img = pyg.transform.flip(self.image,  self.flip, False)
        #pyg.draw.rect(surface, (255, 0, 0), self.rect)
        surface.blit(img, (self.rect.x - (self.offset[0]) * self.scale, self.rect.y - self.offset[1] * self.scale))