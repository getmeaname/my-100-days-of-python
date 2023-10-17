from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(height=600, width=700)
user_bet = screen.textinput(title="Make your bet", prompt="Who will win the race, enter a Color: ")

is_race_on = False

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -30, 10, 50, 90, 130]
all_turtles = []

for i in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-330, y=y_positions[i])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 330:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've Won! The {winning_color} turtle is the winner")
            else:
                print(f"You lose, loser! The {winning_color} turtle is the winner")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
