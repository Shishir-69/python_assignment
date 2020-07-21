import pygame
import sys


def key_down_movement(event, ship, bullet):
    """responds to key down movement"""
    if event.key == pygame.K_RIGHT:
        print("thichhexa")
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        print("thichhexa")
        ship.moving_left = True

    if event.key == pygame.K_SPACE:
        bullet.bullet_state = "fire"


def key_up_movement(event, ship,bullet):
    """responds to key up movement"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
    # if event.key == pygame.K_SPACE:
    #     bullet.bullet_state = "Ready"


def check_key_events(ship,bullet):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            key_down_movement(event, ship, bullet)
        elif event.type == pygame.KEYUP:
            key_up_movement(event, ship, bullet)




def update_game(screen, G_settings, ship,  bullet):
    """updates image on the screen"""
    screen.fill(G_settings.bg_color)
    ship.blitting()
    if bullet.bullet_state == "fire":
        bullet.blitting()
    pygame.display.update()

# class Game_function():
#     def key_down_movement(self):
#         pass
#     def key_up_movement(self):
#         pass
#     def update_game(self,screen,G_settings, ship):
#         """updates image on the screen"""
#         self.screen.fill(G_settings.bg_color)
#         self.ship.blitting()
#         self.pygame.display.update()
