from turtle import Turtle


class Scoreboard:

    def __init__(self):
        self.top = Turtle()
        self.top.penup()
        self.top.color("white")
        self.top.hideturtle()
        with open("new.txt") as file:
            self.highscore = int(file.read())
        self.write_score(0)
    def write_score(self, pts):
        self.top.clear()
        self.top.goto(0, 278)
        self.top.write(f"score : {pts} \tHigh score :{self.highscore} ", True, align="center", font=("Arial", 12, "normal"))

    def write_game_over(self):
        self.top.goto(0, 0)
        self.top.write(f"Game Over", True, align="center", font=("Arial", 16, "normal"))
    def high(self,pts):
        with open("new.txt",mode="w") as file:
            s= str(pts)
            file.write(s)
        self.top.goto(0,-25)
        self.top.write(f"new high score : {pts}", True, align="center", font=("Arial", 16, "normal"))