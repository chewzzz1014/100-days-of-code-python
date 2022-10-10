from turtle import Turtle, Screen

screen = Screen()

# set up the size and position of main window
screen.setup(width=500, height=400)

# pop up window for prompting user input
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

# colors for turtles
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# get the turtles positioned at the starting line
y_positions = [x for x in range(-70, 81, 30)]
for i in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.color(colors[i])
    tim.penup()
    tim.goto(x=-230, y=y_positions[i])




screen.exitonclick()