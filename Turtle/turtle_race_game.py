# Turtle Racing Game

from turtle import Turtle, Screen
import random

Screen().setup(width=500, height=500)    # set up the size and position of the main window.

user_input = Screen().textinput(title="Turtle Racing Game", prompt="Which turtle will win the race ? Enter the color: ")    # taking color an user input.
# print(user_input) # for testing purpose.

is_race_on = False  # Marking is_race_on vriable as False.

colors = ["red", "green", "blue", "yellow", "orange", "purple"] # list of colors.
y_position = [-230, -130, -30, 30, 130, 230]    # list of y-axis positions. (Whereas, x-axis position is constant.)
turtle_list = [] # empty list for storing the instance of the turtles.

# t1 = Turtle(shape="turtle") # while creating an object, passing the shape of the turtle as a parameter.
# t1.color("red")
# t1.penup()
# t1.goto(x = -250+20, y = -250+20)

# t2 = Turtle(shape="turtle") # while creating an object, passing the shape of the turtle as a parameter.
# t2.color("green")
# t2.penup()
# t2.goto(x = -250+20, y = -150+20)

# t3 = Turtle(shape="turtle") # while creating an object, passing the shape of the turtle as a parameter.
# t3.color("blue")
# t3.penup()
# t3.goto(x = -250+20, y = -50+20)

# t4 = Turtle(shape="turtle") # while creating an object, passing the shape of the turtle as a parameter.
# t4.color("yellow")
# t4.penup()
# t4.goto(x = -250+20, y = 50-20)

# t5 = Turtle(shape="turtle") # while creating an object, passing the shape of the turtle as a parameter.
# t5.color("orange")
# t5.penup()
# t5.goto(x = -250+20, y = 150-20)

# t6 = Turtle(shape="turtle") # while creating an object, passing the shape of the turtle as a parameter.
# t6.color("purple")
# t6.penup()
# t6.goto(x = -250+20, y = 250-20)

for index in range(0, 6):   # only 0 to 5 is considered, 6 is exlusive.
    trtl = Turtle(shape="turtle")   # while creating an object, passing the shape of the turtle as a parameter.
    trtl.color(colors[index])   # selecting color from the colors list.
    trtl.penup()    # penup.
    trtl.goto(x = -230, y = y_position[index])  # setting up the position of the turtle.
    turtle_list.append(trtl)    # appending the instances of the turtle to the empty list named as turtle_list.

if user_input:  # if there is some user input then mark is_race_on as True.
    is_race_on = True   # Marking is_race_on varible as True.

while is_race_on:
    for turtle in turtle_list:  # iterating over the instances of the turtle.
        if turtle.xcor() > 230: # checking whether the x coordinates is less than 230.
            is_race_on = False  # Marking is_race_on variable as False.
            winning_turtle = turtle.pencolor()  # storing the color of the turtle in the variable.
            if winning_turtle == user_input.lower():    # checking whether the winning_turtle color is same as user_input color or not.
                print(f"You've won! The {winning_turtle} turtle is the winner.")
            else:
                print(f"You've lost! The {winning_turtle} turtle is the winner.")
        
        distance = random.randint(1, 10)    # both values 1 and 10 is inclusive.
        turtle.forward(distance)    # moving turtle to the forward direction.

Screen().exitonclick()
