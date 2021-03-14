import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
turtle = Player()
carManager = CarManager()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(turtle.moveUp,"Up")


game_is_on = True
while game_is_on:
    if turtle.distance(0,280) < 5:
        turtle.nextLevel()
        scoreboard.levelUp()
        carManager.levelUp()
    carManager.createCar()
    carManager.move()
    for car in carManager.allCars:
        if car.distance(turtle) < 20:
            scoreboard.gameOver()
            game_is_on = False
    time.sleep(0.1)
    screen.update()



screen.exitonclick()