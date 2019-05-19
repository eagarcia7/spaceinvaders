import pygame


class World(object):
    bullets = []
    players = None
    invaders = None
    clock = None
    win = None
    active_player = None

    def __init__(self, title, max_x, max_y, padding, background_image, is_hit_box_enabled=False):
        self.title = title
        self.max_x = max_x
        self.max_y = max_y
        self.padding = padding
        if background_image != "":
            self.bg = pygame.image.load(background_image)
        else:
            self.bg = ""
        self.is_hit_box_enabled = is_hit_box_enabled

    def setup(self, players, invaders):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.win = pygame.display.set_mode((self.max_x, self.max_y))

        # todo How to configure different fonts
        # self.font = pygame.font.SysFont("comicsans", 20)
        pygame.display.set_caption(self.title)

        # prepare players
        self.players = players
        self.invaders = invaders

        # We setup the players
        players.setup(self.win)
        self.active_player = players.players[0]

        # We setup the invaders
        invaders.setup(self.win)

    def add_bullet(self, bullet):
        self.bullets.append(bullet)

    def remove_bullet(self, bullet):
        self.bullets.remove(bullet)
        del bullet

    def redraw(self):
        if self.bg != "":
            self.win.blit(self.bg, (0, 0))
        else:
            self.win.fill((0, 0, 0))

        # render the texts
        # text_score = self.font.render("Score: " + str(self.player.get_score()), 1, (0, 0, 0))
        # text_health = self.font.render("Health: " + str(self.player.get_health()), 1, (0, 0, 0))
        # self.win.blit(text_score, (390, 10))
        # self.win.blit(text_health, (390, 30))

        # draw the players
        self.players.draw(self.win)

        # Draw invaders
        self.invaders.draw(self.win)

        # draw the bullets
        for bullet in self.bullets:
            bullet.draw(self.win)

        pygame.display.update()

    def animate(self):
        # animate invaders
        self.invaders.animate()

        # animate bullets
        for bullet in self.bullets:
            result = bullet.animate()
            if result is False:
                self.remove_bullet(bullet)

