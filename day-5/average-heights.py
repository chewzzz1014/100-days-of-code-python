heights = input("Enter a list of heights: ").split()

sum = 0
for h in heights:
    sum += float(h)

print(f"Average height is {round(sum/len(heights))}cm")