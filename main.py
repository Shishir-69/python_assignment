import pygame
from settings import Settings
from ship import Ship
import game_function as gf
from bullet import Bullet


def run_game():
    pygame.init()
    G_settings = Settings()

    screen = pygame.display.set_mode((G_settings.screen_height, G_settings.screen_width))
    pygame.display.set_caption("BLASTOID")

    # ship class
    ship = Ship(screen, G_settings)
    bullet = Bullet(screen,G_settings,ship)

    running = True
    while running:
        gf.check_key_events(ship,bullet)
        ship.update()
        bullet.update()
        gf.update_game(screen, G_settings, ship, bullet)


run_game()
