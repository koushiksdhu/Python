import turtle
import random

pointer = turtle.Turtle()   # Creating object of the turtle module.
pointer.speed("fastest")    # Speed of the animation.
turtle.colormode(255) # Choosing the color mode of the turtle.

#   Random color function
def random_colors():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return (red, green, blue)   # return tuple i.e., (r, g, b)


for _ in range(int(360 / 5)):
    pointer.color(random_colors()) # selecting random colors from the above random_colors function in the form of tuple.
    pointer.circle(100) # creating circle of radius 100.
    pointer.setheading(pointer.heading() + 5) # shift the arrow to 5 degree angle tilted.
    # pointer.right(5) # does same work as that of line number 20.

turtle.Screen().exitonclick()