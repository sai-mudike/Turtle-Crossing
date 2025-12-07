from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10



class CarManager():
    def __init__(self,screen_width,screen_height):
        self.screen_width=screen_width
        self.screen_height=screen_height
        self.move_speed=STARTING_MOVE_DISTANCE
        self.cars_list=[]
        
    def create_car(self):
        random_chance=random.randint(1,5)
        if random_chance==1:
            new_car=Turtle()
            new_car.penup()
            new_car.shape("square")
            new_car.left(90)
            new_car.shapesize(stretch_wid=2,stretch_len=1)
            new_car.color(random.choice(COLORS))
            new_car.goto(self.screen_width-20,random.randint(-self.screen_height,self.screen_height))
            self.cars_list.append(new_car)
            
    
    def move_car(self):

        for car in self.cars_list:
            car.goto(car.xcor()-self.move_speed,car.ycor())

    def check_collison(self,player):
        for car in self.cars_list:
            if player.distance(car)<25:
                return True
        return False
    def next_level(self):
        self.move_speed+=MOVE_INCREMENT

        
