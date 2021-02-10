from turtle import bgpic, Screen
from player import Player, Goal
from car import Car
from score_board import Score, Level, Information
from time import sleep

# Screen configuration
screen = Screen()
screen.title('pyCrossyRoad')
bgpic('crossyRoadMap.gif')
screen.setup(width=800, height=600)
screen.tracer(0)

# Score Board
score_player = Score()
level_player = Level()
info = Information()

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
    sleep(0.1)

    car.create_car()
    car.move()

    # Calculates the score
    if player.ycor() == -115 or player.ycor() == 110:
        score_player.increase_score()

    # Check if you have reached the goal.
    if goal.distance(player) < 22:
        score_player.increase_score()
        level_player.increase_level()
        player.return_position()
        car.level_up()
        info.winner()

    # Detect collision with a car
    for _car in car.all_cars:
        if _car.distance(player) < 25:
            info.game_over()
            in_game = False

screen.exitonclick()
