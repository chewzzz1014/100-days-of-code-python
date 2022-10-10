import turtle as t
import random

my_turtle = t.Turtle()

colors = ["royal blue", "cyan", "spring green",
          "yellow", "orange red", "purple",
          "saddle brown", "pale green", "dark blue"]
directions = [0, 90, 180, 270]

# use wider pen width
my_turtle.pensize(15)

# alter turtle speed
my_turtle.speed("fastest")

for _ in range(200):
    my_turtle.color(random.choice(colors))
    my_turtle.forward(30)
    my_turtle.setheading(random.choice(directions))