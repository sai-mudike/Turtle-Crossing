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
car=CarManager(320,255)
score_board= Scoreboard()

screen.onkey(turtle.move_up,"w")
screen.onkey(turtle.move_down,"s")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_car()
    if car.check_collison(turtle) ==True:
        game_is_on=False
        score_board.game_over()
    if turtle.ycor()>290:
        turtle.set_position()
        car.next_level()



screen.exitonclick()