import pygame

from misc.files import font, title_font

def draw_pause_screen(surface, screen_width, screen_height):
    "Draw the pause menu"""

    #Surfaces
    pygame.draw.rect(surface, (128, 128, 128, 150), (0, 0, screen_width, screen_height))
    pygame.draw.rect(surface, "black", (200, 150, 1500, 150), 0, 10)

    #Buttons
    resume = pygame.draw.rect(surface, "white", (300, 450, 600, 150), 0, 10)
    quit = pygame.draw.rect(surface, "white", (1000, 450, 600, 150), 0, 10)
    change_characters = pygame.draw.rect(surface, "white", (300, 700, 600, 150), 0, 10)
    change_volume = pygame.draw.rect(surface, "white", (1000, 700, 600, 150), 0, 10)

    #Text
    surface.blit(title_font.render("Game paused.", True, "white"), (750, 190))
    surface.blit(font.render("Resume", True, "black"), (520, 505))
    surface.blit(font.render("Quit", True, "black"), (1250, 505))
    surface.blit(font.render("Change characters", True, "black"), (435, 755))
    surface.blit(font.render("Change volume", True, "black"), (1180, 755))

    #Return the buttons so they can be rendered on screen
    return resume, quit, change_characters, change_volume