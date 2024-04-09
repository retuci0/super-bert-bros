import pygame

from misc.files import platform_image, small_platform_image

class Platform:
    def __init__(self, x, y, w, h, size):
        """Initiate the Platform class."""
        
        if size == "big":
            self.image = platform_image
            self.rect = pygame.Rect(x, y, w, h//4)
            
        elif size == "small":
            self.image = small_platform_image
            self.rect = pygame.Rect(x, y, w, h)
        
        
    def draw(self, screen):
        """Draw the platform on screen."""
        
        screen.blit(self.image, (self.rect.x, self.rect.y))
    
    
    def draw_hitboxes(self, screen):
        """Draw the platforms' hitboxes on screen."""
        
        pygame.draw.rect(screen, (0, 0, 255), self.rect, 2)