# Tkinter is an inbuilt module.
# Tkinter is a Graphical User Interface (GUI) module.
# Tkinter module is converted from other language.

# import tkinter  # importing Tkinter module.
from tkinter import *    # This means from Tkinter module, import every class. -> If we do this then have to specify the module name. i.e., suppose, for calling the Tk() class we don't have to specify tkinter.Tk() rather, only Writing Tk() will do the job.
# there are many classes inside tkinter module. Some of them are: Tk(), Label(), etc.

# window = tkinter.Tk()   # Creating object of the class Tk().
window = Tk()   # Creating object of the class Tk().

window.title("Tkinter Program - My First GUI Program")     # Setting up the title of the program.

window.minsize(width = 800, height = 500)   # Setting up the minimum size of the window.

# LABEL: 

# tkinter has another class named as Label.
label1 = Label(text = "I am Label 1", font = ("Times New Roman", 20, "bold"))  # Font is passed in the form of Tuple.

label1["text"] = "This is Level 1"      # Altering the above text I am Label 1 to This is Level 1.

# The above task can also achieved by using config() method as shown below:
label1.config(text = "This is modified using config() method.")     # By passing keyword argument inside config() method.

label1.pack() # By deafult, the paramter passed his side = "middle"

# label1.pack(side = "left")      # label1 should be placed on the left side of the screen.

# label1.pack(side = "bottom")    # Label1 should be placed on the bottom of the screen.

# label1.pack(side = "top")       # Label1 should be placed on the top of the screen.

# label1.pack(side = "right")     # Label1 should be placed on the right side of the screen.

# pack() method is used to place the components/widgets on the main window/screen.
# pack() method has plenty of functions. For more details, visit official documentation.

# label1.pack(expand = True)  # Label1 should occupy the entire height and width of the entire screen size.

label1.pack()       # pack() method is used to place the components/widgets on the main window/screen.

# BUTTON:

# Event Listener for Button:
def button_clicked():
    print("Button got clicked")     # This will get printed on the console.
    label1["text"] = "Button Clicked"   # To update the label to Button CLicked.
    # OR
    label1.config(text = "Button Clicked")  # To update the label to Button Clicked, the text property is being configured using config() method.
    label1["text"] = input.get()    # get() method used to return the entry in the form of string.

button = Button(text = "Submit", command = button_clicked)       # Creating the object of the class Button with name "Submit".
# command keyword argument is used to call the function/event when the button is clicked. In this the function is "button_clicked()" is not called rather the name of the function is only passed.

button.pack()       # pack() method is used to place the components/widgets on the main window/screen.

# ENTRY COMPONENT: Entry class under the tkinter module.
# Entry class is used for inputfield/textfield.

input = Entry(width = 10)     # Entry is a class under Tkinter module which is used for inputfield/textfield.
# width of the inputfield is being modified using width keyword argument and passing an Integer value onto it.
# get() method used to return the entry in the form of string.
input.pack()        # pack() method is used to place the components/widgets on the screen or window.

window.mainloop()   # Mainloop is used to keep the program running.
# Mainloop just work like that, if I have a while loop with paramter true as shown below:
# while (True):
#   Listening to the window, if the user gives some instructions. For E.g: CLick on a button, or type something on the textfield, etc.
# Mainloop is the thing that will keep the window on the screen.