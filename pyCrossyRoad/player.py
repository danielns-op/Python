from turtle import Turtle, Screen
from random import randint

ACTION_PLAYER = ['char_up.gif', 'char_down.gif', 'char_left.gif', 'char_right.gif', 'char_stop.gif', 'char_finish.gif']
SPEED = 5

for action in ACTION_PLAYER:
    Screen().register_shape(action)

Screen().register_shape('goal.gif')


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape(ACTION_PLAYER[4])
        self.shapesize(stretch_wid=2, stretch_len=2)
        self.goto(360, -260)
        self.return_position()

    def return_position(self):
        self.goto(360, -260)

    def move_up(self):
        self.shape(ACTION_PLAYER[0])
        self.setheading(90)
        # Validate contact with the obstacle when going up.
        if self.ycor() < 80 or 120 < self.ycor() < 280:
            self.forward(SPEED)
        else:
            # Check if it is going over the bridge.
            if -310 < self.xcor() < -290 or -100 < self.xcor() < -70 or \
                    110 < self.xcor() < 130 or 340 < self.xcor() < 360 and self.ycor() < 280:
                self.forward(SPEED)

    def move_down(self):
        self.shape(ACTION_PLAYER[1])
        self.setheading(260)
        # Validate contact with the obstacle when going down.
        if self.ycor() > 130 or 90 > self.ycor() > -280:
            self.forward(SPEED)
        else:
            # Check if it is going over the bridge.
            if -310 < self.xcor() < -290 or -100 < self.xcor() < -70 or \
                    110 < self.xcor() < 130 or 340 < self.xcor() < 360:
                self.forward(SPEED)

    def move_left(self):
        self.shape(ACTION_PLAYER[2])
        self.setheading(180)
        if self.xcor() > -380:
            self.forward(SPEED)

    def move_right(self):
        self.shape(ACTION_PLAYER[3])
        self.setheading(0)
        if self.xcor() < 380:
            self.forward(SPEED)


class Goal(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('goal.gif')
        self.goto((randint(-200, 200), 280))
