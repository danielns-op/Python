from turtle import bgpic, Screen
from player import Player, Goal
from car import Car
from time import sleep

# Screen configuration
screen = Screen()
bgpic('crossyRoadMap.gif')
screen.setup(width=800, height=600)
screen.tracer(0)

# Goal
goal = Goal()
# Player
player = Player()
# Car
car = Car()

# Move Player
screen.listen()
screen.onkeypress(fun=player.move_up, key='w')
screen.onkeypress(fun=player.move_up, key='Up')
screen.onkeypress(fun=player.move_down, key='s')
screen.onkeypress(fun=player.move_down, key='Down')
screen.onkeypress(fun=player.move_left, key='a')
screen.onkeypress(fun=player.move_left, key='Left')
screen.onkeypress(fun=player.move_right, key='d')
screen.onkeypress(fun=player.move_right, key='Right')

in_game = True
while in_game:
    screen.update()
    sleep(0.01)

    car.move()

    if goal.distance(player) < 10:
        player.winner()
        in_game = False


screen.exitonclick()
