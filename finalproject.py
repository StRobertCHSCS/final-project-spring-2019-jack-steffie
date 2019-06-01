import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "final project"
SPRITE_SCALING_CAR = 0.07
SPRITE_SCALING_COIN = 0.02
SPRITE_SCALING_ROCK = 0.02
COIN_COUNT = 50
ENEMY_COUNT = 50


class Coin(arcade.Sprite):
    def update(self):
        self.center_y -= 1
        if self.top < 0:
            self.center_y = random.randrange(SCREEN_HEIGHT + 20,
                                             SCREEN_HEIGHT + 100)
            self.center_x = random.randrange(SCREEN_WIDTH)


class Rock(arcade.Sprite):
    def update(self):
        self.center_y -= 1
        if self.top < 0:
            self.center_y = random.randrange(SCREEN_HEIGHT + 20,
                                             SCREEN_HEIGHT + 100)
            self.center_x = random.randrange(SCREEN_WIDTH)


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.Car_list = None
        self.Coin_list = None
        self.Rock_list = None
        self.Car_sprite = None
        self.score = 0
        self.set_mouse_visible(False)
        self.background = arcade.load_texture("")
        self.sound = arcade.load_sound("MenuTheme.wav")
