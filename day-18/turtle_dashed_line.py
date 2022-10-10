# draw a dashed line using turtle
import turtle as t

my_turtle = t.Turtle()

for _ in range(15):
    my_turtle.forward(10)
    my_turtle.penup()
    my_turtle.forward(10)
    my_turtle.pendown()