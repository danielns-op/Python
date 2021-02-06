from turtle import Turtle

STARTING_POSITION = [(0, 0), (-10, 0), (-20, 0)]
MOVE_DISTANCE = 10


class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITION:
            new_seg = Turtle(shape='square')
            new_seg.shapesize(stretch_wid=0.5)
            new_seg.color('CornflowerBlue')
            new_seg.penup()
            new_seg.goto(position)
            self.snake.append(new_seg)

    def move_forward(self):
        for seg in range(len(self.snake) - 1, 0, -1):
            pos_x = self.snake[seg - 1].xcor()
            pos_y = self.snake[seg - 1].ycor()
            self.snake[seg].goto(pos_x, pos_y)
        self.snake[0].forward(MOVE_DISTANCE)

    def move_up(self):
        pos_x = self.snake[0].xcor()
        pos_y = self.snake[0].ycor()
        self.snake[0].setheading(90)
        for seg in range(1, len(self.snake)):
            if self.snake[seg].xcor() == pos_x and self.snake[seg].ycor() == pos_y:
                self.snake[seg].setheading(90)

    def move_left(self):
        pos_x = self.snake[0].xcor()
        pos_y = self.snake[0].ycor()
        self.snake[0].setheading(180)
        for seg in range(1, len(self.snake)):
            if self.snake[seg].xcor() == pos_x and self.snake[seg].ycor() == pos_y:
                self.snake[seg].setheading(180)

    def move_right(self):
        pos_x = self.snake[0].xcor()
        pos_y = self.snake[0].ycor()
        self.snake[0].setheading(0)
        for seg in range(1, len(self.snake)):
            if self.snake[seg].xcor() == pos_x and self.snake[seg].ycor() == pos_y:
                self.snake[seg].setheading(0)

    def move_down(self):
        pos_x = self.snake[0].xcor()
        pos_y = self.snake[0].ycor()
        self.snake[0].setheading(270)
        for seg in range(1, len(self.snake)):
            if self.snake[seg].xcor() == pos_x and self.snake[seg].ycor() == pos_y:
                self.snake[seg].setheading(270)
