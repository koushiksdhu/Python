# import turtle
# timmy = turtle.Turtle(); #module_name.className()
# print(timmy)

from turtle import Turtle, Screen
ks = Turtle()
ks.shape("turtle") #will change the pointer shape to turtle shapeprint(ks).
ks.color("coral")
ks.forward(40)

#Screen Module
sc = Screen()
print(sc.canvheight)
sc.exitonclick()