class Settings():
    def __init__(self):
        """initializing game settings"""
        self.screen_width = 600
        self.screen_height = 800
        self.bg_color = (91, 91, 91)

        # ship's settings
        self.ship_X_position = 370
        self.ship_Y_position = 480
        self.ship_speed = 2

        #bullet setting
        self.bullet_speed = 1.5
