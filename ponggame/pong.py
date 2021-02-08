# pong.py ####################################################### #
#                                                                 #
# Pong Game                                                       #
#                                                                 #
# Author: Daniel Noronha                                          #
#  Email: danielnoronha.sh@gmail.com                              #
# GitHub: https://github.com/danielns-op/Python/tree/main/pysnake #
# ############################################################### #
from turtle import Screen
from screen_map import LineMiddle
from paddle import PlayerPad, BotPad
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

screen.listen()
screen.onkeypress(fun=player_pad.move_up, key='w')
screen.onkeypress(fun=player_pad.move_down, key='s')

player = True
while player:
    screen.update()
    bot_pad.move_bot()

screen.exitonclick()
