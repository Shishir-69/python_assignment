import pygame

class Bullet():
    def __init__(self,screen,G_settings,ship):
        self.screen = screen
        self.G_settings = G_settings
        self.ship = ship

        self.image = pygame.image.load("bullet.png")
        self.rect = self.image.get_rect()

        #making bullet position in ship position
        self.rect.centerx = self.ship.rect.centerx
        self.rect.bottom = self.ship.rect.top

        self.bullet_state = "ready"
        self.y = float(self.rect.y)

        self.speed_factor = self.G_settings.bullet_speed


    def update(self):
        if self.bullet_state == "fire":
            self.y -= self.speed_factor
            self.rect.y = self.y
        if self.y <= 0:
            self.bullet_state = "ready"
            self.y = self.ship.rect.top



    def blitting(self):
        """used for blitting bullet on screen"""
        self.screen.blit(self.image, self.rect)
