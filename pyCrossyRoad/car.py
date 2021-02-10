from turtle import Turtle, Screen
from random import choice, randint
from time import sleep

CARS = ['blue_car.gif', 'grey_car.gif', 'jeep_green.gif', 'red_car.gif', 'yellow_car.gif']
POS_X = [440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540]
POS_Y = [173, 215, 8, -33, -170, -213]
STARTING_MOVE_DISTANCE = 5
MOVE_ADD = 10

for car in CARS:
    Screen().register_shape(car)


class Car:

    def __init__(self):
        self.car = Turtle()
        self.car.penup()
        self.car.setheading(180)
        self.car.shape(choice(CARS))
        self.pos = (choice(POS_X), choice(POS_Y))
        self.car.goto(self.pos)
        self.pos_x = self.car.xcor()

    def move(self):
        self.pos_x -= 1
        self.car.goto(self.pos_x, self.car.ycor())

