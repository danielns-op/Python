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
from food import Food
from score_board import Score

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
apple = Food()
scoreboard = Score()

screen.listen()
screen.onkeypress(fun=snake.move_up, key='w')
screen.onkeypress(fun=snake.move_up, key='Up')
screen.onkeypress(fun=snake.move_left, key='a')
screen.onkeypress(fun=snake.move_left, key='Left')
screen.onkeypress(fun=snake.move_right, key='d')
screen.onkeypress(fun=snake.move_right, key='Right')
screen.onkeypress(fun=snake.move_down, key='s')
screen.onkeypress(fun=snake.move_down, key='Down')

# Execution
play_game = True
while play_game:
    # It is necessary to use update() and sleep() to mount the
    # image of the snake in motion and not appear with the segmented body.
    screen.update()
    sleep(0.1)
    snake.move_forward()

    # Detect collision with apple.
    if snake.snake_head.distance(apple) < 10:
        apple.refresh()
        scoreboard.increase_score()

    # Detect collision with wall.
    if snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -280 or snake.snake_head.ycor() > 280 or snake.snake_head.ycor() < -280:
        play_game = False

scoreboard.game_over()
screen.exitonclick()
