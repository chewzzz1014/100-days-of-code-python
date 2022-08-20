heights = input("Enter a list of heights: ").split()

highest = heights[0]
for i in range(1, len(heights)):
    if (heights[i]>highest):
        highest = heights[i]

print(f"Highest height is {highest}cm")