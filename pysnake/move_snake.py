class Snake:

    def __init__(self, snake):
        self.snake = snake

    def move_forward(self):
        pos_x = self.snake[0].xcor()
        pos_y = self.snake[0].ycor()
        self.snake[0].forward(9)
        for seg in range(1, len(self.snake)):
            self.snake[seg].goto(pos_x, pos_y)
            pos_x = self.snake[seg].xcor()
            pos_y = self.snake[seg].ycor()

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
