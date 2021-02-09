from turtle import Turtle

MAX_Y = 220
MIN_Y = -220


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.penup()
        self.color('black')
        self.shapesize(stretch_wid=3, stretch_len=0.5)
        self.goto(position)

    def move_up_fp(self):
        pos_y = self.ycor()
        if pos_y < MAX_Y:
            pos_y += 20
            self.goto((-330, pos_y))

    def move_down_fp(self):
        pos_y = self.ycor()
        if pos_y > MIN_Y:
            pos_y -= 20
            self.goto((-330, pos_y))

    def move_up_sp(self):
        pos_y = self.ycor()
        if pos_y < MAX_Y:
            pos_y += 20
            self.goto((330, pos_y))

    def move_down_sp(self):
        pos_y = self.ycor()
        if pos_y > MIN_Y:
            pos_y -= 20
            self.goto((330, pos_y))
