import turtle
import random as r # r is the alias name for the module name random.

turtle.colormode(255);  # Choosing the color mode of the turtle.

colors = ("CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen")    #colors_tuple (Tuples are immutable whereas, lists are mutable.)
directions = (0, 90, 180, 270)  # directions_tuple (Tuples are immutable whereas, lists are mutable)

# Random Colors Function:
def random_colors():
    red = r.randint(0, 255)
    green = r.randint(0, 255)
    blue = r.randint(0, 255)
    color = (red, green, blue)
    return color

pointer = turtle.Turtle()
pointer.width(10) #size of the pen (We can also use pensize instead of width).
pointer.speed("fast") # Animation speed can be either in integer between 1 - 10 (inclusive) or can be 'fast', 'fastest', 'slow', 'slowest' or 'normal'.

for _ in range(100):
    # pointer.color(r.choice(colors)) # selecting random colors.
    pointer.color(random_colors())  # selecting random colors from function random_colors.
    pointer.forward(50) 
    pointer.setheading(r.choice(directions))  # selecting random directions.
    # setheading sets the orientation of the turtle to the angle.

turtle.Screen().exitonclick()  # exit on click.
