from turtle import Turtle, Screen

pointer = Turtle()  # Creating object of the module turtle.

def move_forward(): # mover_forward method.
    pointer.forward(10) # pointer movbbing forward by 10.

Screen().listen()   # Event Listener.
Screen().onkey(key="space", fun=move_forward)   # Listening using onkey function. (move_forward is a higher order fuynction and can be used without parenthesis).

Screen().exitonclick()  # exit on click function.