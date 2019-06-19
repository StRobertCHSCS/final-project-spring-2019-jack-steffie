import arcade
import random

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500
SCREEN_TITLE = "final project"
SPRITE_SCALING_COIN = 0.1
SPRITE_SCALING_ROCK = 0.1
COIN_COUNT = 20
ROCK_COUNT = 20
speed = 5
EXPLOSION_TEXTURE_COUNT = 58


menu_page = 0
game_page = 1
game_over = 2


class Explosion(arcade.Sprite):
    # Add Explosion Class

    explosion_textures = []

    def __init__(self, texture_list):
        super().__init__("images/explosion0000.png")

        self.current_texture = 0
        self.textures = texture_list

    def update(self):

        self.current_texture += 1
        if self.current_texture < len(self.textures):
            self.set_texture(self.current_texture)
        else:
            self.kill()


class Coin(arcade.Sprite):
    # Add Coin Class
    def __init__(self, filename, sprite_scaling):
        super().__init__(filename, sprite_scaling)

        self.change_x = 0
        self.change_y = 0

    def update(self):

        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.change_x *= -1

        if self.right > SCREEN_WIDTH:
            self.change_x *= -1

        if self.bottom < 0:
            self.change_y *= -1

        if self.top > SCREEN_HEIGHT:
            self.change_y *= -1


class Rock(arcade.Sprite):
    # Add Rock Class
    def update(self):
        self.center_y -= 1
        if self.top < 0:
            self.center_y = random.randrange(SCREEN_HEIGHT + 20,
                                             SCREEN_HEIGHT + 100)
            self.center_x = random.randrange(SCREEN_WIDTH)


class MyGame(arcade.Window):
    # MyGame Class
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.Car_list = None
        self.Coin_list = None
        self.Rock_list = None
        self.explosions_list = None
        self.Car_sprite = None
        self.score = 0
        self.car = None
        self.background = arcade.load_texture("timg.jpg")
        self.sound = arcade.load_sound("MenuTheme.wav")
        self.explosion_texture_list = []

        self.set_mouse_visible(True)

        self.page = 0
        self.player_sprite = None

        for i in range(EXPLOSION_TEXTURE_COUNT):
            texture_name = f"images/explosion{i:04d}.png"

            self.explosion_texture_list.append(arcade.load_texture(texture_name))

    def setup(self):
        # setup
        self.Car_list = arcade.SpriteList()
        self.Coin_list = arcade.SpriteList()
        self.Rock_list = arcade.SpriteList()
        self.explosions_list = arcade.SpriteList()
        self.score = 0
        self.car = arcade.AnimatedWalkingSprite()
        self.car.boundary_left = 0
        self.car.boundary_right = 1000

        car_scale = 3

        self.car.stand_right_textures = []
        self.car.stand_right_textures.append(arcade.load_texture("car_middle2.png",
                                                                 scale=car_scale * 0.5))
        self.car.stand_left_textures = []
        self.car.stand_left_textures.append(arcade.load_texture("car_middle2.png",
                                                                scale=car_scale * 0.5))

        self.car.walk_right_textures = []
        self.car.walk_right_textures.append(arcade.load_texture("car_right2.jpg", scale=car_scale))

        self.car.walk_left_textures = []
        self.car.walk_left_textures.append(arcade.load_texture("car_left2.jpg", scale=car_scale))

        self.car.texture_change_distance = 5

        self.car.center_x = 50
        self.car.center_y = 50
        self.car.scale = 1.5
        self.Car_list.append(self.car)

        for i in range(COIN_COUNT):
            coin = Coin("coin.gif", SPRITE_SCALING_COIN)
            # Position the coin
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)
            coin.change_x = random.randrange(-3, 4)
            coin.change_y = random.randrange(-3, 4)

            # Add the coin to the lists
            self.Coin_list.append(coin)

        for i in range(ROCK_COUNT):
            rock = Rock("rock.png", SPRITE_SCALING_ROCK)
            rock.center_x = random.randrange(SCREEN_WIDTH)
            rock.center_y = random.randrange(SCREEN_HEIGHT)
            self.Rock_list.append(rock)

    def draw_menu(self):
        arcade.draw_rectangle_filled(self.width / 2, self.height / 2, 300, 60, arcade.color.DARK_GRAY)
        arcade.draw_text("Start game", self.width / 2 - 110, self.height / 2 - 20, arcade.color.WHITE, 36)

    def draw_game_over(self):
        texture = arcade.load_texture("gg.jpg")
        arcade.draw_texture_rectangle(SCREEN_WIDTH//2, SCREEN_HEIGHT//2, SCREEN_WIDTH, SCREEN_HEIGHT, texture)
        arcade.draw_text("Click to return to main menu", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, arcade.color.AMERICAN_ROSE
                         , 36)

    def draw_game(self):
        # Draw everything
        arcade.draw_texture_rectangle(500, 250, 1000, 500, self.background)
        self.Coin_list.draw()
        self.Rock_list.draw()
        self.Car_list.draw()
        self.explosions_list.draw()
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_draw(self):
        # Draw everything
        arcade.start_render()

        if self.page == 0:
            self.draw_menu()

        elif self.page == 1:
            self.draw_game()

        elif self.page == 2:
            self.draw_game_over()

    def on_mouse_motion(self, position_x, position_y, dx, dy):
        if self.page == 0 or self.page == 2:
            self.position_x = position_x
            self.position_y = position_y

    def on_mouse_press(self, position_x, position_y, button, modifiers):
        if self.page == 0:
            if SCREEN_WIDTH/2 - 30 < self.position_x < SCREEN_WIDTH/2 + 30:
                if SCREEN_HEIGHT/2 - 10 < self.position_y < SCREEN_HEIGHT/2 + 10:
                    self.page = 1

        if self.page == 2:
            self.page = 0
            self.score = 0

    def on_key_press(self, key, modifiers):
        # User Control
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
        # User Control
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.car.velocity[0] = 0
        elif key == arcade.key.A or key == arcade.key.D:
            self.car.velocity[0] = 0

    def update(self, delta_time):
        # Update
        self.Car_list.update()
        self.Car_list.update_animation()
        self.Coin_list.update()
        self.Rock_list.update()
        self.explosions_list.update()
        self.explosions_list = arcade.SpriteList()
        hit_list1 = arcade.check_for_collision_with_list(self.car,
                                                         self.Coin_list)

        for coin in hit_list1:
            coin.kill()
            self.score += 1
            if self.score < 0:
                self.page = 2

        hit_list2 = arcade.check_for_collision_with_list(self.car,
                                                         self.Rock_list)
        for rock in hit_list2:
            if len(hit_list2) > 0:
                explosion = Explosion(self.explosion_texture_list)
                explosion.center_x = hit_list2[0].center_x
                explosion.center_y = hit_list2[0].center_y
                self.explosions_list.append(explosion)
            rock.kill()
            self.score -= 1
            if self.score < 0:
                self.page = 2

        if self.car.center_x < 0:
            self.car.center_x = SCREEN_WIDTH
        if self.car.center_x > SCREEN_WIDTH:
            self.car.center_x = 0


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
