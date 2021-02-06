# pysnake.py #################################################### #
#                                                                 #
# Snake Game                                                      #
#                                                                 #
# Author: Daniel Noronha                                          #
#  Email: danielnoronha.sh@gmail.com                              #
# GitHub: https://github.com/danielns-op/Python/tree/main/pysnake #
# ############################################################### #
from turtle import Screen
from snake import Snake
from time import sleep

# Screen configuration.
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('DarkGray')
screen.title('pySnake Game')
# The tracer() function works in conjunction with the
# update() function in the game loop.
screen.tracer(0)

# Snake characteristics
# Import from Snake class
snake = Snake()

# Execution
play_game = True
while play_game:
    # It is necessary to use update() and sleep() to mount the
    # image of the snake in motion and not appear with the segmented body.
    screen.update()
    sleep(0.1)

    snake.move_forward()

    screen.listen()
    screen.onkey(fun=snake.move_up, key='w')
    screen.onkey(fun=snake.move_left, key='a')
    screen.onkey(fun=snake.move_right, key='d')
    screen.onkey(fun=snake.move_down, key='s')

# Loop up.
screen.exitonclick()
