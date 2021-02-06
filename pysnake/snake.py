from turtle import Turtle

STARTING_POSITION = [(0, 0), (-10, 0), (-20, 0)]
MOVE_DISTANCE = 10


class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake()
        self.snake_head = self.snake[0]

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
        self.snake_head.forward(MOVE_DISTANCE)

    def move_up(self):
        self.snake_head.setheading(90)

    def move_left(self):
        self.snake_head.setheading(180)

    def move_right(self):
        self.snake_head.setheading(0)

    def move_down(self):
        self.snake_head.setheading(270)
