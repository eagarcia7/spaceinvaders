import pygame

from being import Being
from bullet import Bullet


class Player(Being):
    number_of_bullets = 0
    score = 0
    unlimited_bullets = True
    enabled_to_fire = True
    has_fired = False

    # this event will be triggered every second or less to switch the images
    enable_gun_event = pygame.USEREVENT + 2

    def __init__(self, world, x, y, width, height, vel, image, bullet_image, bullet_sound, player_can_fire_multiple_shots,
                 players_shots_per_minute, number_of_bullets=0, unlimited_bullets=True, enabled_to_fire=True):
        self.world = world
        self.vel = vel
        self.is_hit_box_enabled = self.world.is_hit_box_enabled
        self.image = image
        self.bullet_image = bullet_image
        self.bullet_sound = bullet_sound
        self.number_of_bullets = number_of_bullets
        self.unlimited_bullets = unlimited_bullets
        self.enabled_to_fire = enabled_to_fire
        self.player_can_fire_multiple_shots = player_can_fire_multiple_shots
        self.players_shots_per_minute = players_shots_per_minute
        super().__init__(x, y, width, height)

    def setup(self, win):
        pass

    def draw(self, win):
        super().draw(win)
        self.world.win.blit(self.image, (self.x, self.y))

    def add_score(self, value):
        self.score += value

    def fire_bullet(self):
        if self.player_can_fire_multiple_shots is False:
            if self.has_fired is False:
                self.has_fired = True
                bullet = Bullet(self.world, self, self.x, self.y, self.bullet_image, self.bullet_sound)
                self.world.add_bullet(bullet)
        else:
            if self.enabled_to_fire is True:
                self.enabled_to_fire = False
                self.set_time_enable_gun_event(int(1000 / (self.players_shots_per_minute / 60)))
                bullet = Bullet(self.world, self, self.x, self.y, self.bullet_image, self.bullet_sound)
                self.world.add_bullet(bullet)

    def enable_gun(self):
        self.enabled_to_fire = True
        pygame.time.set_timer(self.enable_gun_event, 0)

    def set_time_enable_gun_event(self, time):
        pygame.time.set_timer(self.enable_gun_event, time)
