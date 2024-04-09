import pygame
from misc.files import projectile_image_left, projectile_image_right

class Projectile:
    def __init__(self, x, y, direction, players):
        """Initiate the Projectile class."""
        
        #Movement attributes
        self.rect = pygame.Rect(x, y, 64, 64)
        self.start_pos = x
        self.max_displacement = 960
        self.velocity = 13
        self.direction = direction
        
        if self.direction == "left":
            self.image = projectile_image_left
            
        elif self.direction == "right":
            self.image = projectile_image_right
            
    
    def draw(self, screen):
        """Draw the platform on screen."""
        
        self.move()
        screen.blit(self.image, (self.rect.x, self.rect.y))
    
    def move(self):
        """Constantly move towards the direction the player is facing."""
        
        if self.direction == "left":
            self.rect.x -= self.velocity
            
        elif self.direction == "right":
            self.rect.x += self.velocity
    
    def draw_hitboxes(self, screen):
        """Draw the platforms' hitboxes on screen."""
        
        pygame.draw.rect(screen, (0, 255, 0), self.rect, 2)