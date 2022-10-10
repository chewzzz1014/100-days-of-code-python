import turtle as t
import random

my_turtle = t.Turtle()

# colors = ["royal blue", "cyan", "spring green",
#           "yellow", "orange red", "purple",
#           "saddle brown", "pale green", "dark blue"]
directions = [0, 90, 180, 270]

# color mode from 0-255
t.colormode(255)

# use wider pen width
my_turtle.pensize(15)

# alter turtle speed
my_turtle.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

for _ in range(200):
    # my_turtle.color(random.choice(colors))
    my_turtle.color(random_color())
    my_turtle.forward(30)
    my_turtle.setheading(random.choice(directions))