import pygame


class Input(object):
    switch_image = pygame.USEREVENT + 1
    enable_gun = pygame.USEREVENT + 2

    def __init__(self, world):
        self.world = world
        self.player1 = world.active_player

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == self.switch_image:
                self.world.invaders.switch_image()
            if event.type == self.enable_gun:
                self.world.active_player.enable_gun()

        keys = pygame.key.get_pressed()

        # walk to the left
        if keys[pygame.K_LEFT] and self.player1.x > self.world.padding:
            self.player1.move_left()

        # walk to the right
        elif keys[pygame.K_RIGHT] and self.player1.x < self.world.max_x - self.player1.width - self.world.padding:
            self.player1.move_right()

        # fire bullets
        if keys[pygame.K_SPACE] and self.player1.enabled_to_fire and (
                (self.player1.unlimited_bullets is False and self.player1.number_bullets > 0) or
                self.player1.unlimited_bullets is True):
            # create a bullet and add the bullet
            self.player1.fire_bullet()

        return True
