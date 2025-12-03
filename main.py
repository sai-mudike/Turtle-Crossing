import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

turtle=Player()
car=CarManager(600,600)

screen.onkey(turtle.move_up,"w")
screen.onkey(turtle.move_down,"s")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.move_car()




screen.exitonclick()