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
from move_snake import Snake

# Screen configuration.
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('DarkGray')
screen.title('pySnake Game')

# Snake characteristics
starting_positions = [(0, 0), (-11, 0), (-22, 0)]
snake_body = []

# Defining the movement parameters to be used in the snake class.
move_snake = Snake(snake=snake_body)

for position in starting_positions:
    new_snake_fragment = Turtle(shape='square')
    new_snake_fragment.shapesize(stretch_wid=0.5)
    new_snake_fragment.fillcolor('CornflowerBlue')
    new_snake_fragment.penup()
    new_snake_fragment.goto(position)
    snake_body.append(new_snake_fragment)

# Execution
play_game = True
snake_body[0].fillcolor('blue')
while play_game:
    # It is necessary to use update () and sleep () to mount the
    # image of the snake in motion and not appear with the segmented body.
    screen.update()
    sleep(0.1)
    move_snake.move_forward()
    # for segments in snake_body:
    #     segments.forward(9)
    screen.listen()
    screen.onkey(fun=move_snake.move_up, key='w')
    screen.onkey(fun=move_snake.move_left, key='a')
    screen.onkey(fun=move_snake.move_right, key='d')
    screen.onkey(fun=move_snake.move_down, key='s')

# Loop up.
screen.exitonclick()
