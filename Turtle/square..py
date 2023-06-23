# import turtle # Keyword and Module Name
# square = turtle.Turtle()

# from turtle import * # import everything from the module. Here, * means everything.

# import turtle as t # import: keyword, turtle: moduile, as: keyword, t: alias name 

from turtle import Turtle, Screen # from MODULE import MODULE_METHOD_NAME_THAT_IS_TO_BE_IMPORTED. KEYWORD: from, import
square = Turtle()

square.shape("turtle")
square.color("blue")

# 1st Method: Using Loop.

for _ in range (4):
    square.forward(100)
    square.right(90)
    
# 2nd Method: Manually.

# square.forward(100)
# square.right(90)
# square.forward(100)
# square.right(90)
# square.forward(100)
# square.right(90)
# square.forward(100)
# square.right(90)

# turtle.Screen().exitonclick();
Screen().exitonclick()