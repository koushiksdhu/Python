# W key: Move Forward.
# S key: Move Backward.
# A key: Counter Clockwise / Anti Clockwise.
# D key: Clockwise.
# C key: Clear Drawing.

from turtle import Turtle, Screen

pointer = Turtle()

def move_forward():
    pointer.forward(20)

def move_backward():
    pointer.backward(20)

def counter_clockwise():
    pointer.setheading(pointer.heading() + 10)
    
def clockwise():
    pointer.setheading(pointer.heading() - 10)

def clear():
    #pointer.reset()
    # OR
    pointer.clear()
    pointer.penup()
    pointer.home()
    pointer.pendown()

Screen().listen()
Screen().onkey(key="w", fun=move_forward)
Screen().onkey(key="s", fun=move_backward)
Screen().onkey(key="a", fun=counter_clockwise)
Screen().onkey(key="d", fun=clockwise)
Screen().onkey(key="c", fun=clear)

Screen().exitonclick()