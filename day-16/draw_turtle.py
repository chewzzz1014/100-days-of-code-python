from turtle import Turtle, Screen

my_turtle = Turtle()
print(repr(my_turtle))

# turtle icon in the middle of canvas
my_turtle.shape("turtle")
# brown turtle
my_turtle.color("brown")
# turtle will move by 100
my_turtle.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
# exit when click on window
my_screen.exitonclick()
