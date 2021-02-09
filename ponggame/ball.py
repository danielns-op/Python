from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.fillcolor('DarkGreen')
        self.penup()
        self.move_x = 1
        self.move_y = 1

    def move_ball(self):
        pox_x = self.xcor() + self.move_x
        pos_y = self.ycor() + self.move_y
        self.goto(pox_x, pos_y)

    def reverse_direct_y(self):
        self.move_y *= -1

    def reverse_direct_x(self):
        self.move_x *= -1
