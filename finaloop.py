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
        arcade.draw_text("You must guess number between 1 - 9.", 300, 650, arcade.color.RED, 12)
        self.boxanswer.draw()
        arcade.draw_text(str(self.world.text1) + " " + self.world.text2, 380, 170, arcade.color.RED, 42)

        if self.world.status == 'win':
            self.win.draw()
        if self.world.count <= 0:
            self.lose.draw()


class World(): 
    def __init__(self):
        self.bg = 'images/Screen.png'
        self.number = randint(1,9)
        self.count = 3
        self.text1 = ""
        self.text2 = ""
        self.status = 'not win'

    def on_key_press(self, key, key_modifiers):
        num = 0
        if key == arcade.key.NUM_1:
            num = 1
        if key == arcade.key.NUM_2:
            num = 2
        if key == arcade.key.NUM_3:
            num = 3
        if key == arcade.key.NUM_4:
            num = 4
        if key == arcade.key.NUM_5:
            num = 5
        if key == arcade.key.NUM_6:
            num = 6
        if key == arcade.key.NUM_7:
            num = 7
        if key == arcade.key.NUM_8:
            num = 8
        if key == arcade.key.NUM_9:
            num = 9
        self.text1 = num
        if num < self.number:
            self.text2 = 'too low'
            self.count -= 1
        if num > self.number:
            self.text2 = 'too high'
            self.count -= 1
        if num == self.number:
            self.status = 'win'
        if key == arcade.key.ENTER:
            self.reset()

    def reset(self):
        self.count = 3
        self.number = randint(1,9)
        self.status = 'not win'
        self.text1 = ""
        self.text2 = ""

            
        
 
if __name__ == '__main__':
    window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()

