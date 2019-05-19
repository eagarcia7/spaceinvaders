import pygame

from invader import Invader


# Invaders class
class Invaders(object):
    invaders = []

    # direction = 1 is right and direction = -1 is left
    direction = 1

    # default image_index
    image_index = 0

    # this event will be triggered every second or less to switch the images
    switch_images_event = pygame.USEREVENT + 1

    def __init__(self, w, invaders_max_y, invaders_rows, invaders_columns, invader_width, invader_height,
                 invader_velocity, invader_initial_delay, invader_acceleration, invader_jump_distance, invader_sound,
                 invaders_music, invaders_zone, invaders_images):
        self.world = w
        self.max_y = invaders_max_y
        self.rows = invaders_rows
        self.columns = invaders_columns
        self.width = invader_width
        self.height = invader_height
        self.velocity = invader_velocity
        self.initial_delay = invader_initial_delay
        self.acceleration = invader_acceleration
        self.jump_distance = invader_jump_distance
        self.sound = invader_sound
        self.music = invaders_music
        self.zone = invaders_zone
        self.invaders_images = invaders_images
        self.set_time_switch_image_event(invader_initial_delay)
        pygame.mixer.init(44100, -16, 2, 2048)
        pygame.mixer.music.load(self.music)
        self.sound_mixer = pygame.mixer.Sound(self.sound)

    def setup(self, win):
        pygame.mixer.music.play()
        zone_width = self.zone[1][0] - self.zone[0][0]
        zone_height = self.zone[1][1] - self.zone[0][1]
        y = self.world.padding
        horizontal_separator = int((zone_width - self.world.invaders.width * self.world.invaders.columns) / 10)
        vertical_separator = int((zone_height - self.world.invaders.height * self.world.invaders.rows) / 6)
        for row in range(self.rows):
            x = int((self.world.max_x - zone_width) / 2)
            for column in range(self.columns):
                i = Invader(self.world, x, y, self.world.invaders.width, self.world.invaders.height,
                            self.world.invaders.invaders_images[row])
                self.invaders.append(i)
                i.draw(win)
                x += horizontal_separator + self.world.invaders.width
            y += vertical_separator + self.world.invaders.height

    def set_time_switch_image_event(self, time):
        pygame.time.set_timer(self.switch_images_event, time)

    # This function switch the image of all the invaders as a group
    def switch_image(self):
        self.sound_mixer.play()
        self.image_index = 0 if self.image_index else 1

    def draw(self, win):
        for invader in self.invaders:
            if invader.alive:
                invader.draw(win)
            else:
                self.invaders.remove(invader)
                del invader

    def animate(self):
        # update invaders positions
        hit_wall = False

        for invader in self.invaders:
            # check if some invader hit the boundary
            if invader.x < self.world.padding or invader.x > self.world.max_x - self.world.padding - self.world.invaders.width:
                hit_wall = True
                self.direction *= -1
                self.initial_delay = int(self.initial_delay / self.acceleration)
                self.set_time_switch_image_event(self.initial_delay)
                self.velocity = self.velocity * self.acceleration
                break

        for invader in self.invaders:
            invader.x += self.velocity * self.direction
            if hit_wall:
                invader.y += self.jump_distance * self.acceleration

        # if hit_wall:
        #     self.sound_mixer.play()

