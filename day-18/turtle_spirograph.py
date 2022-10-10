import turtle as t
import random


my_turtle = t.Turtle()

# color mode from 0-255
t.colormode(255)

# alter turtle speed
my_turtle.speed("fastest")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

my_turtle.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range(360//size_of_gap):
        my_turtle.color(random_color())
        my_turtle.circle(100)
        my_turtle.setheading(my_turtle.heading() + size_of_gap)

draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()