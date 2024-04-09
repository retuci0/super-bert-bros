import pygame
from typing import Literal

from misc.characters import *
from misc.files import *

pygame.init()

class Player(pygame.sprite.Sprite):
    def __init__(self, x:int, y:int, character:dict, name:str):
        
        super().__init__()

        #Attributes
        self.name = name
        self.dx = 0
        self.dy = 0
        self.velocity = character["velocity"]
        self.jump_velocity = character["jump_velocity"]
        self.terminal_velocity = character["terminal_velocity"]
        self.gravity = character["gravity"]
        self.hp = character["health"]
        self.projectile_damage = character["projectile_damage"]
        self.lives = 2 #Remaining lives, not total lives, total would be 3
        self.weight = character["weight"]

        #Useless for now (melee attacks stuff)
        self.attacking = False
        self.damage = character["damage"]
        self.crit_chance = character["crit_chance"]

        #Declaring sprites
        self.character = character
        self.status = "idle"
        self.facing = "right"
        self.icon = character["icon"]
        self.walking_sprites_left = character["walking_sprites_left"]
        self.walking_sprites_right = character["walking_sprites_right"]
        self.jumping_sprites_left = character["jumping_sprites_left"]
        self.jumping_sprites_right = character["jumping_sprites_right"]
        self.idle_sprite_left = character["idle_sprite_left"]
        self.idle_sprite_right = character["idle_sprite_right"]
        self.attack_sprite_left = character["attack_sprite_left"]
        self.attack_sprite_right = character["attack_sprite_right"]
        self.damage_sprite_left = character["damage_sprite_left"]
        self.damage_sprite_right = character["damage_sprite_right"]
        self.current_sprites = self.idle_sprite_right
        self.current_sprite = 0
        self.image = self.current_sprites[self.current_sprite]

        #Player hitbox, pygame rect object
        self.rect = pygame.Rect(x, y, self.idle_sprite_left[0].get_width(), self.idle_sprite_left[0].get_height())
        self.rect.topleft = [x, y]
    
    
    def move(self, direction:Literal["left", "right"]):
        """Move around the screen."""
        
        #Check direction to update sprites
        if direction > 0:
            self.facing = "right"
            self.status = "walking"
            
        elif direction < 0:
            self.facing = "left"
            self.status = "walking"
            
        #If direction is 0, don't move
        else:
            self.status = "idle"

        #Set the new dx value
        self.dx = direction * self.velocity
        

    def jump(self, platforms:list):
        "Make the player jump."
        
        #Check if the player's touching a platform, if so set dy to 0
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                self.dy = 0
                return
        
        #If the player's dy is 0, jump
        if self.dy == 0:
            self.dy -= self.jump_velocity
            self.status = "jumping"


    def animate(self):
        """Animate the player when it walks, jumps, attacks, is damaged and stands."""
        #Facing left
        if self.facing == "left":

            #Walking
            if self.status == "walking":
                self.current_sprites = self.walking_sprites_left
                self.current_sprite += 0.2

                if self.current_sprite >= len(self.current_sprites):
                    self.current_sprite = 0
                
                self.image = self.current_sprites[int(self.current_sprite)]
        
            #Jumping
            if self.status == "jumping":
                self.current_sprites = self.jumping_sprites_left
                self.current_sprite += 0.15

                if self.current_sprite >= len(self.current_sprites):
                    self.current_sprite = 0
                
                self.image = self.current_sprites[int(self.current_sprite)]
            
            #Idle
            if self.status == "idle":
                self.image = self.idle_sprite_left[0]
            
            #Damage
            if self.status == "damaged":
                self.image = self.damage_sprite_left[0]
            
            #Attacking
            if self.status == "attacking":
                self.image = self.attack_sprite_left[0]

        #Facing right
        elif self.facing == "right":

            #Walking
            if self.status == "walking":
                self.current_sprites = self.walking_sprites_right
                self.current_sprite += 0.2

                if self.current_sprite >= len(self.current_sprites):
                    self.current_sprite = 0
                
                self.image = self.current_sprites[int(self.current_sprite)]
        
            #Jumping
            if self.status == "jumping":
                self.current_sprites = self.jumping_sprites_right
                self.current_sprite += 0.15

                if self.current_sprite >= len(self.current_sprites):
                    self.current_sprite = 0
                
                self.image = self.current_sprites[int(self.current_sprite)]
            
            #Idle
            if self.status == "idle":
                self.image = self.idle_sprite_right[0]

            #Damage
            if self.status == "damaged":
                self.image = self.damage_sprite_right[0]
            
            #Attacking
            if self.status == "attacking":
                self.image = self.attack_sprite_right[0]
    
    
    def get_hit(self, side:Literal["left", "right"]):
        """Makes knockback work, and plays a funi sound."""
        
        pygame.mixer.Sound.play(damage_sound)
        
        self.status = "damaged"
        
        if side == "left":
            self.dx = -((self.character["health"] - self.hp)) * self.weight
            
        elif side == "right":
            self.dx = ((self.character["health"] - self.hp)) * self.weight
            
        self.dy = -1 * ((self.character["health"] - self.hp) // 10) * self.weight


    def draw_hitboxes(self, screen:pygame.display.set_mode):
        """Draw the player's hitbox, if hitboxes are toggled."""
        
        pygame.draw.rect(screen, (255, 0, 0), self.rect, 2)
        
        
    def update(self, platforms:list):
        """Update the player's position, and handle collisions."""
        
        #Update position using dx for horizonal movement and dy for vertical movement, also including gravity and without exceeding the terminal velocity
        self.dy = min(self.terminal_velocity, self.dy + self.gravity)
        
        self.rect.x += self.dx
        self.rect.y += self.dy

        #Handle collisions
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.dy > 0:
                    self.dy = 0
                    self.rect.bottom = platform.rect.top
        
        #Check for which action the player is doing (tried hard to make the damage sprite work, I guess I am just stupid)
        if self.status != "damaged" and self.status != "attacking":
            if self.dy != 0:
                self.status = "jumping"
                
            else:
                if self.dx != 0:
                    self.status = "walking"
                    
                else:
                    self.status = "idle"
    
                
        #Animate the player
        self.animate()