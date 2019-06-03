import arcade
import random

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500
SCREEN_TITLE = "final project"
SPRITE_SCALING_CAR = 0.07
SPRITE_SCALING_COIN = 0.1
SPRITE_SCALING_ROCK = 0.1
COIN_COUNT = 10
ROCK_COUNT = 10
speed = 5


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
        self.car = None
        self.set_mouse_visible(False)
        self.background = arcade.load_texture("black2.png")
        self.sound = arcade.load_sound("MenuTheme.wav")

    def setup(self):
        self.Car_list = arcade.SpriteList()
        self.Coin_list = arcade.SpriteList()
        self.Rock_list = arcade.SpriteList()
        self.score = 0
        self.car = arcade.AnimatedWalkingSprite()

        car_scale = 3

        self.car.stand_right_textures = []
        self.car.stand_right_textures.append(arcade.load_texture("car_middle.png",
                                                                 scale=car_scale))
        self.car.stand_left_textures = []
        self.car.stand_left_textures.append(arcade.load_texture("car_middle.png",
                                                                scale=car_scale, mirrored=True))

        self.car.walk_right_textures = []
        self.car.walk_right_textures.append(arcade.load_texture("car_right.png", scale=car_scale))

        self.car.walk_left_textures = []
        self.car.walk_left_textures.append(arcade.load_texture("car_left.png", scale=car_scale))

        self.car.texture_change_distance = 5

        self.car.center_x = 50
        self.car.center_y = 50
        self.car.scale = 0.8
        self.Car_list.append(self.car)

        for i in range(COIN_COUNT):
            coin = Coin("coin.gif", SPRITE_SCALING_COIN)
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)
            self.Coin_list.append(coin)

        for i in range(ROCK_COUNT):
            rock = Rock("rock.png", SPRITE_SCALING_ROCK)
            rock.center_x = random.randrange(SCREEN_WIDTH)
            rock.center_y = random.randrange(SCREEN_HEIGHT)
            self.Rock_list.append(rock)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(400, 300, 800, 600, self.background)
        self.Coin_list.draw()
        self.Rock_list.draw()
        self.Car_list.draw()
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.car.velocity[0] = -speed
        elif key == arcade.key.A:
            self.car.velocity[0] = -speed
        elif key == arcade.key.RIGHT:
            self.car.velocity[0] = speed
        elif key == arcade.key.D:
            self.car.velocity[0] = speed
        elif key == arcade.key.SPACE:
            arcade.play_sound(self.sound)

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.car.velocity[0] = 0
        elif key == arcade.key.A or key == arcade.key.D:
            self.car.velocity[0] = 0

    def update(self, delta_time):
        self.Car_list.update()
        self.Car_list.update_animation()
        self.Coin_list.update()
        self.Rock_list.update()
        hit_list1 = arcade.check_for_collision_with_list(self.car,
                                                         self.Coin_list)
        for coin in hit_list1:
            coin.kill()
            self.score += 1

        hit_list2 = arcade.check_for_collision_with_list(self.car,
                                                         self.Rock_list)
        for rock in hit_list2:
            rock.kill()
            self.score -= 1


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
