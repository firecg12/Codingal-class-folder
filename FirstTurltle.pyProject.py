import turtle
import random
import time

# Set up the screen
screen = turtle.Screen()
screen.setup(980, 860)

# Create a turtle
polygon = turtle.Turtle()
polygon.speed(3)  # 0-10 only, no decimals

# Polygon settings
num_sides = 4
side_length = 90
angle = 90

# Draw a square
for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)

# Colors list
colors = [
    "red", "orange", "yellow", "green", "blue", "purple", "pink",
    "cyan", "magenta", "gold", "turquoise", "lime", "indigo",
    "brown", "gray", "white", "#3b3636"
]

# Keep swapping background color and rotating the turtle
while True:
    screen.bgcolor(random.choice(colors))  # pick random background color
    polygon.forward(side_length)
    polygon.right(angle)
    time.sleep(1)  # wait 2 seconds


    