# draw triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon using turtle, all nested together

import turtle as t
import random

my_turtle = t.Turtle()

colors = ["royal blue", "cyan", "spring green",
          "yellow", "orange red", "purple",
          "saddle brown", "pale green", "dark blue"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        my_turtle.forward(100)
        my_turtle.right(angle)

for i in range(3, 11):
    my_turtle.color(random.choice(colors))
    draw_shape(i)