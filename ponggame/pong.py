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
from paddle import PlayerPad, BotPad
from ball import Ball
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
player_pad = PlayerPad()
bot_pad = BotPad()

# Ball
pong_ball = Ball()

# Score
player_score = Score()
player_score.score_player()
bot_score = Score()
bot_score.score_bot()

screen.listen()
screen.onkeypress(fun=player_pad.move_up, key='w')
screen.onkeypress(fun=player_pad.move_down, key='s')

player = True
winner = False
while player:
    screen.update()
    pong_ball.move_ball()
    bot_pad.move_bot()
    # Detect collision with wall.
    if pong_ball.xcor() > 330:
        winner = True
        player = False
    elif pong_ball.xcor() < -330:
        player = False

if winner:
    player_score.winner_game()
else:
    player_score.game_over()

screen.exitonclick()
