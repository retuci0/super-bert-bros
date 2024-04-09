import pygame

#To change the key bound to a certain action, simply find it here and replace it with the key's name
#You can find all keys and their respective pygame name listed here: http://cs.roanoke.edu/Fall2013/CPSC120A/pygame-1.9.1-docs-html/ref/key.html

#Player 1
K_player1_left = pygame.K_a
K_player1_right = pygame.K_d
K_player1_jump = pygame.K_SPACE
K_player1_projectile = pygame.K_e

#Player 2
K_player2_left = pygame.K_LEFT
K_player2_right = pygame.K_RIGHT
K_player2_jump = pygame.K_UP
K_player2_projectile = pygame.K_RCTRL

#Other
K_hitbox = pygame.K_b
K_pause = pygame.K_ESCAPE
K_quit = pygame.K_0