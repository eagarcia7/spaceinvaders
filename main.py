import pygame

from world import World
from players import Players
from input import Input
from invaders import Invaders

# Loading parameters
world_width = 1000
world_height = 1000
world_padding = 50

players_number = 1
players_shots_per_minute = 600
player_can_fire_multiple_shots = False
player_width = 28
player_height = 20
player_initial_x = world_width / 2
player_initial_y = world_height - world_padding - player_height
player_velocity = 5
player_image = pygame.image.load('images/player.png')

bullet_image = pygame.image.load('images/player_bullet.png')
bullet_sound = 'sounds/shoot.wav'

invader_width = 32
invader_height = 20
invader_velocity = 2
invader_initial_delay = 1000
invader_acceleration = 1.1
invader_jump_distance = 30
invader_sound = 'sounds/fastinvader2.wav'
invaders_rows = 6
invaders_columns = 11
invaders_music = 'sounds/spaceinvaders.mpeg'
invaders_zone = [[200, 50], [800, 550]]
invaders_max_y = 250
invaders_images = [[pygame.image.load('images/invader1A.png'), pygame.image.load('images/invader1B.png')],
                   [pygame.image.load('images/invader2A.png'), pygame.image.load('images/invader2B.png')],
                   [pygame.image.load('images/invader3A.png'), pygame.image.load('images/invader3B.png')],
                   [pygame.image.load('images/invader1A.png'), pygame.image.load('images/invader1B.png')],
                   [pygame.image.load('images/invader2A.png'), pygame.image.load('images/invader2B.png')],
                   [pygame.image.load('images/invader3A.png'), pygame.image.load('images/invader3B.png')]]

# We create the world (screen and context)
w = World("First Game", world_width, world_height, world_padding, '')

# Now we create our player (single player only)
players = Players(w, players_number, player_initial_x, player_initial_y, player_width, player_height, player_velocity,
                  player_can_fire_multiple_shots, players_shots_per_minute, player_image, bullet_image, bullet_sound)

# Then we crete out collection of space invaders
invaders = Invaders(w, invaders_max_y, invaders_rows, invaders_columns, invader_width, invader_height, invader_velocity,
                    invader_initial_delay, invader_acceleration, invader_jump_distance, invader_sound, invaders_music,
                    invaders_zone, invaders_images)

# We setup our world with our players and space invaders
w.setup(players, invaders)

# We create the interface to get all user inputs

i = Input(w)

# We loop until the user decides to end the game
run = True
while run:
    # Set the refresh ratio
    w.clock.tick(30)

    # read any other input from the user
    run = i.events()

    # change the world
    w.animate()

    # now repaint it
    w.redraw()

pygame.quit()
