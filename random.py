import arcade
import arcade.keys
from random import randint


SCREEN_WIDTH = 962
SCREEN_HEIGHT = 723
BOX_POS = [481,600,200]


class whatnumber(arcade.Window):
	def _init_(self, width, height):
		super()._init_(width, height)
		self.world = World()
		#arcade.set_background_color(arcade.color.BLACK)
		self.boxstart = arcade.Sprite('images/textboxstartresize.png')
        self.boxstart.set_position(BOX_POS[0], BOX_POS[1])
        self.boxanswer = arcade.Sprite('images/answerbox.png')
        self.boxanswer.set_position(BOX_POS[0], BOX_POS[2])


        def on_draw(self):
            arcade.start_render()
            self.boxstart.draw()
            time.sleep(2)
            arcade.draw_text(str(You must guess number between 1 - 10.), 481, 600, arcade.color.RED, 12, width =200, align="center", anchor_x="center", anchor_y="center")
            time.sleep(3)
            arcade.draw_text(str(You have 3 times.), 481, 580, arcade.color.RED, 12, width =200, align="center", anchor_x="center", anchor_y="center")
            time.sleep(1)
            self.boxanswer.draw()
            arcade.draw_text(str('Take a guess (push number and enter)'), 481, 180, arcade.color.RED, 12, width =200, align="center", anchor_x="center", anchor_y="center")
            world.guess()



class World():
    def __init__(self):
        number = random.randint(1, 10)
        count = 0

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.NUM_1:
            


    def guess():
        while count < 3:
            guess = input()
            guess = int(guess)
            count = count+1
            if guess < number:
                arcade.draw_text(str(too low), 481, 560, arcade.color.RED, 12, width =200, align="center", anchor_x="center", anchor_y="center")
            if guess > number:
                arcade.draw_text(str(too high), 481, 540, arcade.color.RED, 12, width =200, align="center", anchor_x="center", anchor_y="center")
            if guess == number:
                break
        if guess == number:
            count = str(count)
            self.win = arcade.Sprite('images/win.png')
            self.win.set_position(481, 360)
        if guess != number:
            number =  str(number)
            self.win = arcade.Sprite('images/lose.png')
            self.win.set_position(481, 360)
