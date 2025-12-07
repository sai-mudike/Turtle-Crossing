from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self, ):
        super().__init__()
        self.level=1
        self.penup()
        self.hideturtle()
        self.color('black')
        self.goto(-270,260)
        self.write(arg=f"Level:{self.level} ",font=("Courier", 18, "normal"))

    def next_level(self):
        self.level+=1
        self.clear()
        self.write(arg=f"Level:{self.level} ",font=("Courier", 18, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write(arg=f"Game Over",font=FONT,align="center")
    
