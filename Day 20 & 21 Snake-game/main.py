import time
from turtle import Screen
from food import Food
from snake import Snake
from scoreboard import ScoreBoard
new_position = [(0, 0), (-20, 0), (-40, 0)]

segments = []

# Setting up world
screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("The snake game")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

#     Detect Collision with food
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    # Detect Collision with wall
    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < -280:
        is_game_on = False
        score.game_over()

    # Detect tail collision
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            is_game_on = False
            score.game_over()

screen.exitonclick()
