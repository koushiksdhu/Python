from turtle import Turtle, Screen
import random as r

n = int(input("Enter the number: "))

pointer = Turtle()
pointer.color("red")
pointer.shape("arrow")

colors = ["red", "green", "blue", "yellow", "black", "magenta", "cyan", "orange"]
          
# # Method 1:

# i = n+1
# while(i < 11):
#     for _ in range (i):
#         pointer.forward(100)
#         pointer.right(360 / (i - 1)) # Angle(in degree): 360 / number_of_sides.
#     i += 1


# Method 2:

def shapes(n):
    angle = 360 / n     # Angle(in degree): 360 / number_of_sides.
    for k in range (n):
        pointer.forward(100)
        pointer.right(angle)
for i in range(3, n+1):
    pointer.color(colors[i - 3])
    shapes(i)
    
        


Screen().exitonclick()
