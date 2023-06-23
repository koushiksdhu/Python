import turtle, random

pointer = turtle.Turtle()
turtle.colormode(255)   # colormode of the turtle.
pointer.speed("fastest")    # speed of the animation.

def random_color(): # Generating random colors.
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b);   # returning r, g, b in the form of tuple.

pointer.color("#ffffff")    # outer color of the circle.
y = 0.0 # initializing the y-axis position.

# Method 1: Using circle() function.

# for _ in range (10):
#     for _ in range (10):
#         pointer.fillcolor(random_color())   # filling color in the circle.
#         pointer.begin_fill()    # begin filling the color.
#         pointer.circle(10)  # drawing circle using turtle.
#         pointer.end_fill()  # ending the color filling.
#         pointer.penup() # penup.
#         pointer.forward(30) # moving forward.
#         pointer.pendown()   # pendown.
        
#     pointer.penup() # penup.
#     y -= 30 # moving y axis to -30.
#     pointer.setpos(0.0, y)  # setting position of the arrow by the updated value of the y-axis.
#     pointer.pendown()   # pendown.

# Method 2: Using dot() function.

for _ in range(10):
    for _ in range(10):
        pointer.dot(20, random_color())
        pointer.penup()    
        pointer.forward(30)
        pointer.pendown()
    pointer.penup()
    y += 30.0
    pointer.setpos(0.0, y)
    pointer.pendown()
    
turtle.Screen().exitonclick()