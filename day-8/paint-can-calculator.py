# 1 can of paint can cover 5 square meters of wall.
# Given a random height and width of wall, calculate how many cans of paint you'll need to buy.
import math
def calc_paint_can(h, w, coverage):
    cans =  math.ceil(h*w/coverage)
    print(f"You'll need {cans} cans of paint")

h = float(input("Height of wall: "))
w = float(input("Width of wall: "))
calc_paint_can(h, w, 5)

