from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('white')
        self.fillcolor('DarkGreen')

    def move_ball(self):
        self.forward(1)

    def sense_n(self):
        self.setheading(90)

    def sense_nne(self):
        self.setheading(60)

    def sense_ne(self):
        self.setheading(30)

    def sense_e(self):
        self.setheading(0)

    def sense_se(self):
        self.setheading(330)

    def sense_sse(self):
        self.setheading(300)

    def sense_s(self):
        self.setheading(270)

    def sense_ssw(self):
        self.setheading(240)

    def sense_sw(self):
        self.setheading(210)

    def sense_w(self):
        self.setheading(180)

    def sense_nw(self):
        self.setheading(150)

    def sense_nnw(self):
        self.setheading(120)

