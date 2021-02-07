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
            self.add_segment(position)

    def add_segment(self, position):
        new_seg = Turtle(shape='square')
        new_seg.shapesize(stretch_wid=0.5)
        new_seg.color('CornflowerBlue')
        new_seg.penup()
        new_seg.goto(position)
        self.snake.append(new_seg)

    def extend(self):
        self.add_segment(self.snake[-1].position())

    def move_forward(self):
        for seg in range(len(self.snake) - 1, 0, -1):
            pos_x = self.snake[seg - 1].xcor()
            pos_y = self.snake[seg - 1].ycor()
            self.snake[seg].goto(pos_x, pos_y)
        self.snake_head.forward(MOVE_DISTANCE)

    def move_up(self):
        # If the direction of movement is downwards, it cannot go upwards.
        if self.snake_head.heading() != 270:
            self.snake_head.setheading(90)

    def move_left(self):
        # If the direction of movement is to the right, he cannot go to the left.
        if self.snake_head.heading() != 0:
            self.snake_head.setheading(180)

    def move_right(self):
        # If the direction of movement is to the left, he cannot go to the right.
        if self.snake_head.heading() != 180:
            self.snake_head.setheading(0)

    def move_down(self):
        # If the direction of movement is upwards, it cannot go downwards.
        if self.snake_head.heading() != 90:
            self.snake_head.setheading(270)
