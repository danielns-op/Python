# pong.py ######################################################## #
#                                                                  #
# Pong Game                                                        #
#                                                                  #
# Author: Daniel Noronha                                           #
#  Email: danielnoronha.sh@gmail.com                               #
# GitHub: https://github.com/danielns-op/Python/tree/main/ponggame #
# ################################################################ #
from turtle import Screen
from screen_map import LineMiddle, Score
from ball import Ball
from paddle import Paddle
from random import randint
from time import sleep

# Screen configuration
screen = Screen()
screen.setup(width=700, height=500)
screen.bgcolor('CornflowerBlue')
screen.title('Pong Game')
screen.tracer(0)

# Middle line
line = LineMiddle()
line.draw_line()

# Paddles
first_player = Paddle((-330, 0))
second_player = Paddle((330, randint(-200, 200)))

# Ball
pong_ball = Ball()

# Score
player_score = Score()
bot_score = Score()
bot_score.score_bot()
player_score.score_player()

screen.listen()
screen.onkeypress(fun=first_player.move_up_fp, key='w')
screen.onkeypress(fun=first_player.move_down_fp, key='s')
screen.onkeypress(fun=second_player.move_up_sp, key='Up')
screen.onkeypress(fun=second_player.move_down_sp, key='Down')

player = True
winner = False
while player:
    screen.update()
    pong_ball.move_ball()

    # Detect collision with wall.
    if pong_ball.ycor() > 230 or pong_ball.ycor() < -230:
        pong_ball.reverse_direct_y()

    # Detect collision with paddle.
    if pong_ball.distance(second_player) < 30 and pong_ball.xcor() > 320 or \
            pong_ball.distance(first_player) < 30 and pong_ball.xcor() < -320:
        pong_ball.reverse_direct_x()

    # Detect realized point.
    if pong_ball.xcor() < -340:
        bot_score.score += 1
        if bot_score.score == 5:
            player = False
        bot_score.score_bot()
        pong_ball.refresh_ball()
    elif pong_ball.xcor() > 340:
        player_score.score += 1
        if player_score.score == 5:
            winner = True
            player = False
        player_score.score_player()
        pong_ball.refresh_ball()

if winner:
    player_score.winner_game()
else:
    player_score.game_over()

screen.exitonclick()
