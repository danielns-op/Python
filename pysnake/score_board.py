from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 20, 'normal')


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('black')
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(arg=f'Score: {self.score}', align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.color('red')
        self.goto(0, 0)
        self.write('GAME OVER', align=ALIGNMENT, font=('Courier', 50, 'normal'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()