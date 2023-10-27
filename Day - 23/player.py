import turtle
from turtle import Turtle

STARTING_POS = (0, -280)
MOVE_DIS = 10
FINISH_LINE = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("black")
        self.goto(STARTING_POS)
        self.setheading(90)

    def move_up(self):
        self.forward(MOVE_DIS)

    def go_to_start(self):
        self.goto(STARTING_POS)

    def is_finished(self):
        if self.ycor() > FINISH_LINE:
            return True
        else:
            return False
