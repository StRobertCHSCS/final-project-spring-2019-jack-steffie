import arcade

width = 1000
height = 500

menu_page = 0
game_page = 1
store_page = 2
game_over = 3


class MyGame(arcade.Window):
    coin_count = 0
    highest_score = 0

    def __init__(self, width, height):
        super().__init__(width, height)

        self.set_mouse_visible(True)

        arcade.set_background_color(arcade.color.DARK_SLATE_GRAY)

        self.page = 0
        self.player_sprite = None

    def draw_menu(self):
        arcade.draw_rectangle_filled(self.width/2, self.height/2, 300, 60, arcade.color.DARK_GRAY)
        arcade.draw_text("Start game", self.width/2 - 110, self.height/2 - 20, arcade.color.WHITE, 36)
        arcade.draw_rectangle_filled( self.width/2, self.height/3, 300, 60, arcade.color.DARK_BLUE_GRAY)
        arcade.draw_text("Store", self.width /2, 100, arcade.color.WHITE, 18)
        arcade.draw_text("Highest Score: ", self.width*4/5, self.height*2/3, arcade.color.BLACK)

    def draw_store(self):
        arcade.draw_text("Coin: ", self.width*3/4, self.height*5/6, arcade.color.WHITE, 18)

    def draw_game_over(self):
        arcade.draw_text("Game Over", self.width/2, self.width/2, arcade.color.BRICK_RED, 54)
        arcade.draw_text("Click to return to main menu", self.width/2, self.width/2, arcade.color.AMERICAN_ROSE, 36)

    def on_draw(self):
        arcade.start_render()

        if self.page == 0:
            self.draw_menu()

        elif self.page == 2:
            self.draw_store()

        elif self.page == 3:
            self.draw_game_over()

    def on_mouse_motion(self, position_x, position_y, dx, dy):
        if self.page == 0 or self.page == 2:
            self.position_x = position_x
            self.position_y = position_y

    def on_mouse_press(self, position_x, position_y, button, modifiers):
        if self.page == 0:
            if self.width/2 - 30 < self.position_x < self.width/2 + 30:
                if self.height/2 - 10 < self.position_y < self.height/2 + 10:
                    self.page = 1
                elif self.height/3 - 10 < self.position_y < self.height/3 + 10:
                    self.page = 2
        if self.page == 3:
            self.page = 0


def main():
    MyGame(width, height)
    arcade.run()


if __name__ == "__main__":
    main()
