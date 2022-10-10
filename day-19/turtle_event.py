from turtle import Turtle, Screen

my_turtle = Turtle()

screen = Screen()

def move_forward():
    my_turtle.forward(10)

def move_backward():
    my_turtle.backward(10)

def turn_left():
    new_heading = my_turtle.heading() + 10
    my_turtle.setheading(new_heading)

def turn_right():
    new_heading = my_turtle.heading() - 10
    my_turtle.setheading(new_heading)

def clear():
    my_turtle.clear()
    my_turtle.penup()
    my_turtle.home()
    my_turtle.pendown()

# listen to events
screen.listen()

# add event listeners
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")

screen.exitonclick()

