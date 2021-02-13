import pandas as pd
from turtle import Screen, Turtle
from time import sleep

FILE = pd.read_csv('./27_states_brazil.csv')
ALL_STATES = FILE['state'].to_list()

FONT = ('Arial', 10, 'bold')
FONT_SCORE = ('Arial', 20, 'bold')


class States:

    def __init__(self):
        self.state = Turtle()
        self.state.penup()
        self.states_files = FILE.to_dict()
        self.pos_x = 0
        self.pos_y = 0
        self.hits = []

    def asking(self):
        question = Screen().textinput(f'{len(self.hits)}/27 Acertos', 'Informe um estado: ')
        if not question:
            self.exit_quiz()
        for state in ALL_STATES:
            if state == question:
                self.hits.append(state)
                self.pos_x = self.states_files['x'][ALL_STATES.index(state)]
                self.pos_y = self.states_files['y'][ALL_STATES.index(state)]
                self.state.goto(self.pos_x, self.pos_y)
                self.state.write(arg=state, align='center', font=FONT)
                return True

    def show_errors(self):
        for state in ALL_STATES:
            if state not in self.hits:
                self.pos_x = self.states_files['x'][ALL_STATES.index(state)]
                self.pos_y = self.states_files['y'][ALL_STATES.index(state)]
                self.state.goto(self.pos_x, self.pos_y)
                self.state.color('red')
                self.state.write(arg=state, align='center', font=FONT)

    def exit_quiz(self):
        self.state.goto(0, 0)
        self.state.color('DarkBlue')
        self.state.write(arg='Ate a próxima!', align='center', font=('Arial', 30, 'bold'))
        sleep(3)
        exit(0)


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.life = 6
        self.penup()
        self.goto(0, 250)
        self.write(arg=f'Pontuação: {self.score}\tVidas: {self.life}', align='center', font=FONT_SCORE)

    def increase_score(self):
        self.score += 10

    def decrease_life(self):
        self.life -= 1

    def update(self):
        self.clear()
        self.write(arg=f'Score: {self.score}\tLife: {self.life}', align='center', font=FONT_SCORE)

    def you_won(self):
        self.goto(0, 50)
        self.color('chocolate')
        self.write(arg='Parabéns, você sabe tudo!', align='center', font=('Arial', 30, 'bold'))
        sleep(3)
        exit(0)

    def game_over(self):
        self.goto(0, 0)
        self.color('red')
        self.write(arg='Game Over', align='center', font=('Arial', 40, 'bold'))
