from turtle import Turtle
from random import randint, choice
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.allCars = []
        self.carSpeed = STARTING_MOVE_DISTANCE

    def createCar(self):
        randChance = randint(1,6)
        if randChance == 1:
            newCar = Turtle("square")
            newCar.shapesize(stretch_wid=1, stretch_len=2)
            newCar.color(choice(COLORS))
            newCar.penup()
            self.randY = randint(-250, 250)
            newCar.goto(300, self.randY)
            self.allCars.append(newCar)

    def move(self):
        for car in self.allCars:
            car.backward(self.carSpeed)
    def levelUp(self):
        self.carSpeed += MOVE_INCREMENT

