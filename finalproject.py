import arcade


class MyGame(arcade.Window):

    width = 800
    height = 600

    coin_count = 0

    menu_page = 0
    game_page = 1
    store_page = 2
    game_over = 3

    def __init__(self, width, height):
        super().__init(width, height)

        self.page = 0

    def draw_menu(self):
        arcade.draw_rectangle_filled(self.width/2, self.height/2, 30, 10)
        arcade.draw_text("Start game", self.width/2, 300, arcade.color.ASH_GREY, 36)
        arcade.draw_rectangle_filled( self.width/2, self.height/3, 30, 10)
        arcade.draw_text("Store", self.width /2, 100, arcade.color.BLACK, 18)

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
            self.player_sprite.centre_x = position_x
            self.player_sprite.centre_y = position_y

    def on_mouse_press(self, position_x, position_y, button, modifiers):

        if self.page == 0:
            if self.width/2 - 30 < self.position_x < self.width/2 + 30:
                if self.height/2 - 10 < self.position_y < self.height/2 + 10:
                    self.page = 1
                elif self.height/3 - 10 < self.position_y < self.height/3 + 10:
                    self.page = 2
        if self.page == 3:
            self.page = 0
