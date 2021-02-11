from turtle import Turtle

with open('data_score.txt') as file:
    HIGH_SCORE = file.read()
file.close()

ALIGNMENT = 'center'
FONT = ('Courier', 20, 'normal')


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(HIGH_SCORE)
        self.color('black')
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def update_high_score(self):
        with open('data_score.txt') as file:
            data_score = file.read()
        file.close()
        self.high_score = int(data_score)

    def update_score(self):
        self.clear()
        self.update_high_score()
        self.write(arg=f'Score: {self.score}\tHigh Score: {self.high_score}', align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            with open('data_score.txt', 'w') as data_file:
                data_file.write(f'{self.score}')
            data_file.close()
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()


class GameOver(Turtle):

    def __init__(self):
        super().__init__()
        self.color('red')
        self.goto(0, 0)
        self.write('GAME OVER', align=ALIGNMENT, font=('Courier', 50, 'normal'))

