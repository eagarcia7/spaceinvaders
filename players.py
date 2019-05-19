from player import Player


class Players(object):
    players = []
    gameplay_in_turns = False

    def __init__(self, w, players_number, player_initial_x, player_initial_y, player_width, player_height,
                 player_velocity, player_can_fire_multiple_shots, players_shots_per_minute, player_image,
                 bullet_image, bullet_sound):
        self.world = w
        self.players_number = players_number
        self.player_initial_x = player_initial_x
        self.player_initial_y = player_initial_y
        self.player_width = player_width
        self.player_height = player_height
        self.player_velocity = player_velocity
        self.player_image = player_image
        self.bullet_image = bullet_image
        self.bullet_sound = bullet_sound
        self.player_can_fire_multiple_shots = player_can_fire_multiple_shots
        self.players_shots_per_minute = players_shots_per_minute

    def setup(self, win):
        # How many players?
        if self.players_number == 1:
            # Create the players and add them to the array
            player = Player(self.world, self.player_initial_x, self.player_initial_y, self.player_width,
                            self.player_height, self.player_velocity, self.player_image, self.bullet_image,
                            self.bullet_sound, self.player_can_fire_multiple_shots, self.players_shots_per_minute)
            player.setup(win)
            self.players.append(player)

        else:
            # Together or in turns?
            pass

    def draw(self, win):
        if self.players_number == 1:
            player = self.players[0]
            if player.alive:
                player.draw(win)
            else:
                self.players.remove(player)
                del player
        else:
            pass
