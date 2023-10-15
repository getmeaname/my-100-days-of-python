# import colorgram
#
# rgb_colors = []
#
# colors = colorgram.extract("image.png", 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
#
# # sorted(colors, key=lambda c: c.hsl.h)
#
# print(rgb_colors)

# Refer document for better understanding https://docs.python.org/3/library/turtle.html#turtle.setworldcoordinates

import turtle as t
from turtle import Screen
from random import *

color_list = [(224, 234, 229), (176, 48, 79), (42, 98, 146), (205, 161, 94), (223, 210, 102), (137, 90, 64),
              (177, 164, 38), (109, 176, 207), (212, 131, 173), (227, 73, 49), (201, 75, 117), (88, 105, 192),
              (28, 143, 89), (124, 218, 207), (120, 43, 71), (94, 158, 65), (227, 170, 187), (131, 184, 161),
              (48, 187, 202), (172, 187, 222), (232, 173, 164), (154, 209, 219), (100, 51, 43), (34, 64, 115),
              (44, 80, 79), (215, 207, 37), (52, 58, 66)]

t.colormode(255)
tim = t.Turtle()
tim.speed('fastest')
tim.penup()
tim.hideturtle()

tim.setheading(215)
tim.forward(350)
tim.setheading(0)

num_of_dots = 100

for dot_count in range(1, num_of_dots + 1):
    tim.dot(20, choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(360)

screen = Screen()
screen.exitonclick()
