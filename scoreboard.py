from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.goto(-200,270)
        self.hideturtle()
        self.color("black")
        self.updateLevel()
    def updateLevel(self):
        self.write(f"Level: {self.level}",align= ALIGNMENT,font=FONT)

    def levelUp(self):
        self.level +=1
        self.clear()
        self.updateLevel()
    def gameOver(self):
        self.goto(0,0)
        self.write(f"Game Over! You reached Level {self.level}",align= ALIGNMENT,font=FONT)
        self.goto(0,0)
