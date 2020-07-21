import pygame


class Ship():
    """includes all the components of ship """

    def __init__(self, screen, G_settings):
        self.screen = screen
        self.G_settings = G_settings

        self.image = pygame.image.load("player.png")
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()


        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.moving_right = False
        self.moving_left = False

        self.center = float(self.rect.centerx)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.G_settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.center -= self.G_settings.ship_speed

        self.rect.centerx = self.center


    def blitting(self):
        """used for blitting the image on screen"""
        self.screen.blit(self.image, self.rect)
