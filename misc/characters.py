import pygame

pygame.init()
pygame.font.init()


################################################################################################
########################################## >> BERT << ##########################################
################################################################################################

BERT = {
    "name": "Bert",
    "description": "average human.",
    "health": 100,
    "damage": 5,
    "projectile_damage": 3,
    "velocity": 5,
    "jump_velocity": 11,
    "crit_chance": 0.2,
    "gravity": 0.5,
    "terminal_velocity": 20,
    "weight": 1, #The less the value is, the less knockback it will take
    "walking_sprites_right": [
        (pygame.image.load("assets/images/bert/walk/0.png")),
        (pygame.image.load("assets/images/bert/walk/1.png")),
        (pygame.image.load("assets/images/bert/walk/2.png")),
        (pygame.image.load("assets/images/bert/walk/3.png")),
        (pygame.image.load("assets/images/bert/walk/4.png"))
    ],
    "walking_sprites_left": [],
    "jumping_sprites_right": [
        (pygame.image.load("assets/images/bert/jump/0.png")),
        (pygame.image.load("assets/images/bert/jump/1.png")),
        (pygame.image.load("assets/images/bert/jump/2.png")),
        (pygame.image.load("assets/images/bert/jump/3.png")),
        (pygame.image.load("assets/images/bert/jump/4.png"))
    ],
    "jumping_sprites_left": [],
    "idle_sprite_right": [(pygame.image.load("assets/images/bert/idle/0.png"))],
    "idle_sprite_left": [],
    "attack_sprite_right": [(pygame.image.load("assets/images/bert/attack/0.png"))],
    "attack_sprite_left": [],
    "damage_sprite_right": [(pygame.image.load("assets/images/bert/damage/0.png"))],
    "damage_sprite_left": [],
    "icon": pygame.image.load("assets/images/bert/icon.png")
}

for sprite in BERT["walking_sprites_right"]:
    inverted_sprite = pygame.transform.flip(sprite, True, False)
    BERT["walking_sprites_left"].append(inverted_sprite)

for sprite in BERT["jumping_sprites_right"]:
    inverted_sprite = pygame.transform.flip(sprite, True, False)
    BERT["jumping_sprites_left"].append(inverted_sprite)

BERT["idle_sprite_left"] = [(pygame.transform.flip(BERT["idle_sprite_right"][0], True, False))]

BERT["attack_sprite_left"] = [(pygame.transform.flip(BERT["attack_sprite_right"][0], True, False))]

BERT["damage_sprite_left"] = [(pygame.transform.flip(BERT["damage_sprite_right"][0], True, False))]


################################################################################################
######################################### >> BERROTA << ########################################
################################################################################################

BERROTA = {
    "name": "Berrota",
    "description": "lightweight skinny mf, moves faster than your mom in my bed.",
    "health": 90,
    "damage": 5,
    "projectile_damage": 3,
    "velocity": 7,
    "jump_velocity": 13,
    "crit_chance": 0.35,
    "gravity": 0.5,
    "terminal_velocity": 17,
    "weight": 1.5,
    "walking_sprites_right": [
        (pygame.image.load("assets/images/berrota/walk/0.png")),
        (pygame.image.load("assets/images/berrota/walk/1.png")),
        (pygame.image.load("assets/images/berrota/walk/2.png")),
        (pygame.image.load("assets/images/berrota/walk/3.png")),
        (pygame.image.load("assets/images/berrota/walk/4.png"))
    ],
    "walking_sprites_left": [],
    "jumping_sprites_right": [
        (pygame.image.load("assets/images/berrota/jump/0.png")),
        (pygame.image.load("assets/images/berrota/jump/1.png")),
        (pygame.image.load("assets/images/berrota/jump/2.png")),
        (pygame.image.load("assets/images/berrota/jump/3.png")),
        (pygame.image.load("assets/images/berrota/jump/4.png"))
    ],
    "jumping_sprites_left": [],
    "idle_sprite_right": [(pygame.image.load("assets/images/berrota/idle/0.png"))],
    "idle_sprite_left": [],
    "attack_sprite_right": [(pygame.image.load("assets/images/berrota/attack/0.png"))],
    "attack_sprite_left": [],
    "damage_sprite_right": [(pygame.image.load("assets/images/berrota/damage/0.png"))],
    "damage_sprite_left": [],
    "icon": pygame.image.load("assets/images/berrota/icon.png")
}

for sprite in BERROTA["walking_sprites_right"]:
    inverted_sprite = pygame.transform.flip(sprite, True, False)
    BERROTA["walking_sprites_left"].append(inverted_sprite)

for sprite in BERROTA["jumping_sprites_right"]:
    inverted_sprite = pygame.transform.flip(sprite, True, False)
    BERROTA["jumping_sprites_left"].append(inverted_sprite)

BERROTA["idle_sprite_left"] = [(pygame.transform.flip(BERROTA["idle_sprite_right"][0], True, False))]

BERROTA["attack_sprite_left"] = [(pygame.transform.flip(BERROTA["attack_sprite_right"][0], True, False))]

BERROTA["damage_sprite_left"] = [(pygame.transform.flip(BERROTA["damage_sprite_right"][0], True, False))]


################################################################################################
########################################## >> LORC << ##########################################
################################################################################################

LORC = {
    "name": "Lorc",
    "description": "heavy tank, his fat will tank all your attacks, his only weakness is gravity.",
    "health": 200,
    "damage": 5,
    "projectile_damage": 3,
    "velocity": 3,
    "jump_velocity": 7.5,
    "crit_chance": 0.1,
    "gravity": 0.72,
    "terminal_velocity": 25,
    "weight": 0.5,
    "walking_sprites_right": [
        (pygame.image.load("assets/images/lorc/walk/0.png")),
        (pygame.image.load("assets/images/lorc/walk/1.png")),
        (pygame.image.load("assets/images/lorc/walk/2.png")),
        (pygame.image.load("assets/images/lorc/walk/3.png")),
        (pygame.image.load("assets/images/lorc/walk/4.png"))
    ],
    "walking_sprites_left": [],
    "jumping_sprites_right": [
        (pygame.image.load("assets/images/lorc/jump/0.png")),
        (pygame.image.load("assets/images/lorc/jump/1.png")),
        (pygame.image.load("assets/images/lorc/jump/2.png")),
        (pygame.image.load("assets/images/lorc/jump/3.png")),
        (pygame.image.load("assets/images/lorc/jump/4.png"))
    ],
    "jumping_sprites_left": [],
    "idle_sprite_right": [(pygame.image.load("assets/images/lorc/idle/0.png"))],
    "idle_sprite_left": [],
    "attack_sprite_right": [(pygame.image.load("assets/images/lorc/attack/0.png"))],
    "attack_sprite_left": [],
    "damage_sprite_right": [(pygame.image.load("assets/images/lorc/damage/0.png"))],
    "damage_sprite_left": [],
    "icon": pygame.image.load("assets/images/lorc/icon.png")
}

for sprite in LORC["walking_sprites_right"]:
    inverted_sprite = pygame.transform.flip(sprite, True, False)
    LORC["walking_sprites_left"].append(inverted_sprite)

for sprite in LORC["jumping_sprites_right"]:
    inverted_sprite = pygame.transform.flip(sprite, True, False)
    LORC["jumping_sprites_left"].append(inverted_sprite)

LORC["idle_sprite_left"] = [(pygame.transform.flip(LORC["idle_sprite_right"][0], True, False))]

LORC["attack_sprite_left"] = [(pygame.transform.flip(LORC["attack_sprite_right"][0], True, False))]

LORC["damage_sprite_left"] = [(pygame.transform.flip(LORC["damage_sprite_right"][0], True, False))]


################################################################################################
########################################## >> JORDI << #########################################
################################################################################################

JORDI = {
    "name": "Jordi",
    "description": "strong but fragile, i was going to make a yo mamma joke but i'll better shut up.",
    "health": 80,
    "damage": 10,
    "projectile_damage": 5,
    "velocity": 5.1,
    "jump_velocity": 11,
    "crit_chance": 0.3,
    "gravity": 0.5,
    "terminal_velocity": 17,
    "weight": 1.2,
    "walking_sprites_right": [
        (pygame.image.load("assets/images/jordi/walk/0.png")),
        (pygame.image.load("assets/images/jordi/walk/1.png")),
        (pygame.image.load("assets/images/jordi/walk/2.png")),
        (pygame.image.load("assets/images/jordi/walk/3.png")),
        (pygame.image.load("assets/images/jordi/walk/4.png"))
    ],
    "walking_sprites_left": [],
    "jumping_sprites_right": [
        (pygame.image.load("assets/images/jordi/jump/0.png")),
        (pygame.image.load("assets/images/jordi/jump/1.png")),
        (pygame.image.load("assets/images/jordi/jump/2.png")),
        (pygame.image.load("assets/images/jordi/jump/3.png")),
        (pygame.image.load("assets/images/jordi/jump/4.png"))
    ],
    "jumping_sprites_left": [],
    "idle_sprite_right": [(pygame.image.load("assets/images/jordi/idle/0.png"))],
    "idle_sprite_left": [],
    "attack_sprite_right": [(pygame.image.load("assets/images/jordi/attack/0.png"))],
    "attack_sprite_left": [],
    "damage_sprite_right": [(pygame.image.load("assets/images/jordi/damage/0.png"))],
    "damage_sprite_left": [],
    "icon": pygame.image.load("assets/images/jordi/icon.png")
}

for sprite in JORDI["walking_sprites_right"]:
    inverted_sprite = pygame.transform.flip(sprite, True, False)
    JORDI["walking_sprites_left"].append(inverted_sprite)

for sprite in JORDI["jumping_sprites_right"]:
    inverted_sprite = pygame.transform.flip(sprite, True, False)
    JORDI["jumping_sprites_left"].append(inverted_sprite)

JORDI["idle_sprite_left"] = [(pygame.transform.flip(JORDI["idle_sprite_right"][0], True, False))]

JORDI["attack_sprite_left"] = [(pygame.transform.flip(JORDI["attack_sprite_right"][0], True, False))]

JORDI["damage_sprite_left"] = [(pygame.transform.flip(JORDI["damage_sprite_right"][0], True, False))]