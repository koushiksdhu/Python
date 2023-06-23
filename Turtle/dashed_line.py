from turtle import Turtle, Screen

dl = Turtle()

for _ in range (20):
    dl.forward(10)
    dl.penup() # penup command.
    dl.forward(10)
    dl.pendown() # pendown command.
    
Screen().exitonclick()
    