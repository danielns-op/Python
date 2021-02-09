from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 25, 'normal')


class LineMiddle:
    def __init__(self):
        self.middle_line = []
        self.draw_line()

    def draw_line(self):
        for y in range(-235, 250, 45):
            self.line_add_seg(position=y)

    def line_add_seg(self, position):
        new_seg = Turtle(shape='square')
        new_seg.shapesize(stretch_wid=1, stretch_len=0.5)
        new_seg.color('DarkGrey')
        new_seg.penup()
        new_seg.goto(x=0, y=position)
        self.middle_line.append(new_seg)


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('gray0')
        self.penup()
        self.hideturtle()

    def update_score(self):
        self.write(arg=f'{self.score}', align=ALIGNMENT, font=FONT)

    def score_player(self):
        self.goto(-100, 210)
        self.update_score()

    def score_bot(self):
        self.goto(100, 210)
        self.update_score()

    def winner_game(self):
        self.color('orange')
        self.goto(0, 0)
        self.write(arg='You Won!!!', align=ALIGNMENT, font=('Arial', 50, 'bold'))

    def game_over(self):
        self.color('red')
        self.goto(0, 0)
        self.write(arg='Game Over\nYou lose.', align=ALIGNMENT, font=('Arial', 50, 'bold'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
