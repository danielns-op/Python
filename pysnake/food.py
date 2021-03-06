from turtle import Turtle, Screen
from random import randint

Screen().register_shape('apple.gif')


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('apple.gif')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('red')
        self.speed('fastest')
        x_random = randint(-250, 250)
        y_random = randint(-250, 250)
        self.goto(x_random, y_random)
        self.refresh()

    def refresh(self):
        x_random = randint(-250, 250)
        y_random = randint(-250, 250)
        self.goto(x_random, y_random)
