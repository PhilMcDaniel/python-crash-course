import pygame

class Ship:
    """A class to manage the ship."""

    def __init__(self,ai_game):
        """Initialize the ship and its starting position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #load the ship image and get its rect
        self.image = pygame.image.load('ship.bmp')
        self.rect = self.image.get_rect()

        #start ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # store decimal value for ships horizontal position
        self.x = float(self.rect.x)

        #movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """update ship position based on movement flag"""
        if self.moving_right:
            self.x += self.settings.ship_speed
        if self.moving_left:
            self.x -= self.settings.ship_speed

        #update rect from self.x
        self.rect.x = self.x

    def blitme(self):
        """draw the ship at its current location."""
        self.screen.blit(self.image,self.rect)