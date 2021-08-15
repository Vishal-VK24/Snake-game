from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.4, stretch_wid=0.4)
        self.color("blue")
        self.speed("fastest")
        self.new_food()

    def new_food(self):
        x = random.randint(-340, 340)
        y = random.randint(-280, 270)
        self.goto(x=x, y=y)
