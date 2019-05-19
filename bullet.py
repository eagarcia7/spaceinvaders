import pygame


class Bullet(object):
    gravity = False
    isFired = True
    direction_vector = [[0, 0], [0, -1]]

    def __init__(self, w, source, x, y, image, sound, initial_velocity=10):
        self.world = w
        self.source = source
        self.x = x
        self.y = y
        self.image = image
        self.sound = sound
        self.initial_velocity = initial_velocity
        self.horizontal_velocity = (self.direction_vector[1][0] - self.direction_vector[0][0]) * self.initial_velocity
        self.vertical_velocity = (self.direction_vector[1][1] - self.direction_vector[0][1]) * self.initial_velocity
        self.offset_x = int(source.width / 2)
        self.offset_y = int(source.height / 2)
        pygame.mixer.init(44100, -16, 2, 2048)
        self.sound_mixer = pygame.mixer.Sound(self.sound)
        self.sound_mixer.play()
        # todo play hit sound

    def animate(self):
        # check for out of boundaries
        if self.out_of_boundaries():
            self.source.has_fired = False
            return False

        # check for collision
        if self.hasCollided():
            # todo destroy invader
            self.source.has_fired = False
            return False

        self.x += self.horizontal_velocity
        self.y += self.vertical_velocity

        return True

    def draw(self, win):
        win.blit(self.image, (self.x + self.offset_x, self.y + self.offset_y))

    def out_of_boundaries(self):
        if 0 < self.x < self.world.max_x and 0 < self.y < self.world.max_y:
            return False
        else:
            return True

    def hasCollided(self):
        pass
