from turtle import Turtle
from random import randint

MAX_Y = 220
MIN_Y = -220


class Paddle:

    def __init__(self):
        self.pad = Turtle(shape='square')
        self.pad.penup()
        self.pad.color('black')
        self.pad.shapesize(stretch_wid=3, stretch_len=0.5)


class PlayerPad(Paddle):

    def __init__(self):
        super().__init__()
        self.pad.goto((-330, 0))
        self.pos_x = self.pad.xcor()

    def move_up(self):
        pos_y = self.pad.ycor()
        if pos_y != MAX_Y:
            pos_y += 10
            self.pad.goto((self.pos_x, pos_y))

    def move_down(self):
        pos_y = self.pad.ycor()
        if pos_y != MIN_Y:
            pos_y -= 10
            self.pad.goto((self.pos_x, pos_y))


class BotPad(Paddle):

    def __init__(self):
        super().__init__()
        self.pad.goto((330, randint(-200, 200)))
        self.pos_x = self.pad.xcor()

    def move_bot(self):
        pos_y = self.pad.ycor()
        if pos_y != MIN_Y:
            pos_y += 1
        self.pad.goto((self.pos_x, pos_y))