class Settings:
    """A class to store all settings for Alien Invasion game."""
#resources
#https://github.com/ehmatthes/pcc_2e/
    def __init__(self):
        """Initialize the game's settings."""
        #screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        #ship settings
        self.ship_speed = 1.5