import random

import colorgram
import turtle as t

def extract_colors():
    rgb_colors = []
    colors = colorgram.extract("image.jpg", 30)

    for c in colors:
        r = c.rgb.r
        g = c.rgb.g
        b = c.rgb.b
        rgb_colors.append((r, g, b))

    return rgb_colors

rgb_colors = extract_colors()

# remove colors that are likely to be the background of image
rgb_colors.pop(0)
rgb_colors.pop(0)
color_list = rgb_colors[:]


# recreate the color in image into dots
my_turtle = t.Turtle()
t.colormode(255)

# don't show the line, just show the dots
my_turtle.penup()

# hide the turtle (that look like pointer)
my_turtle.hideturtle()

my_turtle.setheading(225)
my_turtle.forward(250)
my_turtle.setheading(0)

number_of_dots = 100

for i in range(1, number_of_dots+1):
    my_turtle.dot(20, random.choice(color_list))
    my_turtle.forward(50)

    # create new row
    if i % 10 == 0:
        my_turtle.setheading(90)
        my_turtle.forward(50)
        my_turtle.setheading(180)
        my_turtle.forward(500)
        my_turtle.setheading(0)


screen = t.Screen()
screen.exitonclick()
