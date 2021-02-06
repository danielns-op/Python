# pysnake.py ################################################## #
#                                                               #
# Snake Game                                                    #
#                                                               #
# Author: Daniel Noronha                                        #
#  Email: danielnoronha.sh@gmail.com                            #
# GitHub:
# ############################################################# #
from turtle import Screen, Turtle
from time import sleep

# Screen configuration.
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('DarkGray')
screen.title('pySnake Game')


# Functions
def move_up():
    pos_x = snake_body[0].xcor()
    pos_y = snake_body[0].ycor()
    snake_body[0].setheading(90)
    for seg in range(1, len(snake_body)):
        if snake_body[seg].xcor() == pos_x and snake_body[seg].ycor() == pos_y:
            snake_body[seg].setheading(90)


# Snake characteristics
starting_positions = [(0, 0), (-11, 0), (-22, 0)]
snake_body = []

for position in starting_positions:
    new_snake_fragment = Turtle(shape='square')
    new_snake_fragment.shapesize(stretch_wid=0.5)
    new_snake_fragment.fillcolor('CornflowerBlue')
    new_snake_fragment.penup()
    new_snake_fragment.goto(position)
    snake_body.append(new_snake_fragment)

# Execution
play_game = True
while play_game:
    # It is necessary to use update () and sleep () to mount the
    # image of the snake in motion and not appear with the segmented body.
    screen.update()
    sleep(0.1)
    for segments in snake_body:
        segments.forward(9)
    screen.listen()
    screen.onkey(fun=move_up, key='w')

# Loop up.
screen.exitonclick()
