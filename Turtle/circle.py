from turtle import Turtle, Screen

circle = Turtle()
circle.color("red")

for _ in range(360):
    circle.forward(1) # Move forward to 1 space.
    circle.right(1) # Turn right to 1 degree.

Screen().exitonclick()
