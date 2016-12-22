import arcade
import arcade.key
from random import randint
 
SCREEN_WIDTH = 962
SCREEN_HEIGHT = 723
 
class GameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.BLACK)
        self.boxstart = arcade.Sprite('images/boxstart.png')
        self.boxstart.set_position(481, 600)
        self.boxanswer = arcade.Sprite('images/answerbox.png')
        self.boxanswer.set_position(481, 200)

        self.win = arcade.Sprite('images/win.jpg')
        self.win.set_position(481, 361)
        self.lose = arcade.Sprite('images/lose.jpg')
        self.lose.set_position(481, 361)

        self.world = World()

    def on_key_press(self, key, key_modifiers):
        self.world.on_key_press(key, key_modifiers)

    def on_draw(self):
        arcade.start_render()
        self.bg_img = arcade.Sprite(self.world.bg)
        self.bg_img.set_position(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        self.bg_img.draw()
        self.boxstart.draw()
        arcade.draw_text("You must guess number between 1 - 9.", 481, 600, arcade.color.RED, 12)
        self.boxanswer.draw()
        if self.world.status == 'win':
            self.win.draw()
        

class World(): 
    def __init__(self):
        self.bg = 'images/Screen.png'
        number = randint(1,9)
        self.count = 3
        self.text1 = ""
        self.text2 = ""
        self.status = 'not win'

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.NUM_1:
            if 1 < number:
                text2 = 'too low'
            if 1 > number:
                text2 = 'too high'
            if 1 == number:
                self.status = 'win'
        
 
if __name__ == '__main__':
    window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()

