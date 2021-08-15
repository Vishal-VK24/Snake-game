from turtle import Turtle

MOVEMENT = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.body = []
        self.create_snake()
        self.head = self.body[0]

    def create_snake(self):
        x = 0
        y = 0
        for i in range(0, 3):
            t = Turtle()
            t.penup()
            t.shape("square")
            t.color("white")
            t.goto(x=x, y=y)
            x = x - 20
            self.body.append(t)

    def move_snake(self):
        for i in range(len(self.body) - 1, 0, -1):
            x_coord = self.body[i - 1].xcor()
            y_coord = self.body[i - 1].ycor()
            self.body[i].goto(x_coord, y_coord)
        self.body[0].forward(MOVEMENT)

    def up(self):
        if self.body[0].heading() != DOWN:
            self.body[0].setheading(UP)

    def down(self):
        if self.body[0].heading() != UP:
            self.body[0].setheading(DOWN)

    def left(self):
        if self.body[0].heading() != RIGHT:
            self.body[0].setheading(LEFT)

    def right(self):
        if self.body[0].heading() != LEFT:
            self.body[0].setheading(RIGHT)

    def add(self):
        t = Turtle()
        t.penup()
        t.shape("square")
        t.color("white")
        n = len(self.body)
        t.goto(x=self.body[n-1].xcor(), y=self.body[n-1].ycor())
        self.body.append(t)
