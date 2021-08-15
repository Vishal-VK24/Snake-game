from turtle import Screen
import time
from snake import Snake
from foodd import Food
from score import Scoreboard
s = Screen()
s.title("snake game")
s.setup(height=600, width=720)
s.bgcolor("black")
s.tracer(0)
s.listen()
snake = Snake()
food = Food()
s.onkey(snake.up, "Up")
s.onkey(snake.down, "Down")
s.onkey(snake.left, "Left")
s.onkey(snake.right, "Right")
check = True
score = Scoreboard()
pts = 0
while check:
    s.update()
    time.sleep(0.05)
    snake.move_snake()
    if snake.head.distance(food) < 15:
        food.new_food()
        pts = pts+1
        score.write_score(pts)
        snake.add()
    if snake.head.xcor() > 360 or snake.head.xcor() < -360 or snake.head.ycor() < -300 or snake. head.ycor() > 300:
        check = False
        if score.highscore < pts:
            score.high(pts)
        score.write_game_over()
    for i in snake.body[1:]:
        if snake.head.distance(i) < 8:
            check = False
            if score.highscore < pts:
                score.high(pts)
            score.write_game_over()
s.exitonclick()
