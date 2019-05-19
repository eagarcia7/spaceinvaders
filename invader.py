from being import Being


class Invader(Being):

    def __init__(self, w, x, y, width, height, images):
        self.world = w
        self.images = images
        super().__init__(x, y, width, height)

    def setup(self):
        pass

    def draw(self, win):
        super().draw(win)
        image_index = self.world.invaders.image_index
        win.blit(self.images[image_index], (self.x, self.y))

