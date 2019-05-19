import pygame


class Being(object):
    x = 0
    y = 0
    width = 0
    height = 0
    hit_box = ()
    health_bar = []
    is_hit_box_enabled = False
    is_health_bar_enabled = False
    hit_box_gap = []
    health = 100
    alive = True
    value = 0
    vel = 0

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def set_hit_box(self):
        self.hit_box = (
            self.x + self.hit_box_gap[3], self.y + self.hit_box_gap[0],
            self.width - self.hit_box_gap[1] - self.hit_box_gap[3],
            self.height - self.hit_box_gap[0] - self.hit_box_gap[2])

    def set_health_bar(self):
        middle_point = (self.width - self.hit_box_gap[1] - self.hit_box_gap[3]) * self.health / 100
        self.health_bar = [(self.x + self.hit_box_gap[3], self.y + self.hit_box_gap[0],
                            middle_point, 2),
                           (self.x + self.hit_box_gap[3] + middle_point, self.y + self.hit_box_gap[0],
                            self.width - self.hit_box_gap[1] - self.hit_box_gap[3] - middle_point, 2)]

    def draw(self, win):
        if self.is_health_bar_enabled:
            self.set_health_bar()
            # draw the health line
            # todo Fix the bars
            pygame.draw.rect(win, (0, 255, 0), self.health_bar[0])
            pygame.draw.rect(win, (255, 0, 0), self.health_bar[1])

        if self.is_hit_box_enabled:
            self.set_hit_box()
            pygame.draw.rect(win, (255, 0, 0), self.hit_box, 1)

    def hit(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.alive = False

    def move_right(self):
        self.x += self.vel

    def move_left(self):
        self.x -= self.vel
