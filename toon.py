import pygame

class Toon:
    """A class to manage the toon."""

    def __init__(self, ai_game):
        """Initialize the toon and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the Toon image and get its rect.
        self.image = pygame.image.load('images/toon.bmp')
        self.rect = self.image.get_rect()

        # Start each new toon at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw the toon at its current location."""
        self.screen.blit(self.image, self.rect)