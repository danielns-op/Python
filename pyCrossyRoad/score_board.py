from turtle import Turtle
from time import sleep

FONT = ('Arial', 20, 'normal')
FONT_INFO = ('Arial', 80, 'normal')


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(-340, 260)
        self.write(arg=f'Score: {self.score}', align='left', font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f'Score: {self.score}', align='left', font=FONT)


class Level(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(340, 260)
        self.write(arg=f'Level: {self.level}', align='right', font=FONT)

    def increase_level(self):
        self.level += 1
        self.clear()
        self.write(arg=f'Level: {self.level}', align='right', font=FONT)


class Information(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def winner(self):
        self.goto(0, 50)
        self.color('IndianRed4')
        self.write(arg='Level UP', align='center', font=FONT_INFO)
        sleep(2)
        self.clear()

    def game_over(self):
        self.goto(0, 50)
        self.color('Red')
        self.write(arg='Game Over', align='center', font=FONT_INFO)
