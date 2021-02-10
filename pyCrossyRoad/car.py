from turtle import Turtle, Screen
from random import choice, randint
from time import sleep

CARS = ['blue_car.gif', 'grey_car.gif', 'jeep_green.gif', 'red_car.gif', 'yellow_car.gif']
POS_X = [400, 420, 440, 460, 480, 500]
POS_Y = [173, 215, 8, -33, -170, -213]
STARTING_MOVE_DISTANCE = 5
MOVE_ADD = 10

for stile in CARS:
    Screen().register_shape(stile)


class Car:

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def create_car(self):
        # Car generation control, it will only be generated if the number 15 is drawn.
        chance = randint(1, 15)
        if chance == 6:
            new_car = Turtle(shape=(choice(CARS)))
            new_car.shapesize(stretch_wid=4, stretch_len=1)
            new_car.penup()
            new_car.goto(choice(POS_X), choice(POS_Y))
            self.all_cars.append(new_car)

    def level_up(self):
        self.car_speed += MOVE_ADD
