from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10



class CarManager(Turtle):
    def __init__(self,screen_width,screen_height):
        super().__init__()
        self.screen_width=screen_width
        self.screen_height=screen_height
        self.penup()
        self.shape("square")
        self.left(90)
        self.shapesize(stretch_wid=2,stretch_len=1)
        self.color(random.choice(COLORS))
        self.goto(screen_width-20,random.randint(-screen_height,screen_height))
    
    def move_car(self):
        self.goto(self.xcor()-STARTING_MOVE_DISTANCE,self.ycor())

        
