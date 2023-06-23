from tkinter import *

# Widgets: Label, Button, Entry, Text Entry Box, Spinbox(Counter), Scale(Slider), Checkbutton(on and off), Radiobutton, Listbox.

# Creating a new window and configuration:
window = Tk()
window.title("Widgets Example")
window.minsize(width = 500, height = 500)

# Label:
label = Label(text = "Label 1")
label.config(text = "This is configured label")
label["text"] = "This is updated label"
label.pack()

# Button:
def button_action():
    print("Button got clicked.")

button = Button(text = "Click Here", command = button_action)       # calls button_action() method, when pressed.
button.pack()

# Entries:
entry = Entry(width = 30)
entry.insert(END, string = "Some text to begin with....")       # Add some text to begin with.
print(entry.get())      # Gets text in entry.
entry.pack()

# Text:
text = Text(width = 30, height = 5)     # height = Number of lines.
text.focus()        # Put cursor in the textbox.
text.insert(END, "Example of multiline text entry....")      # Adds some text to begin with.
print(text.get("1.0", END))     # Get's current value in textbox at line 1, character 0.
text.pack()

# Spinbox:
def spinbox_action():
    print(spinbox.get())    # Gets current value in spinbox.

spinbox = Spinbox(from_= 0, to = 10, width = 5, command = spinbox_action)   # Note: from_ (with underscore) is the keyword here.
spinbox.pack()

# Scale: Called with Current Scale Value.
def scale_action(value):
    print(value)
    
scale = Scale(from_ = 0, to = 100, command = scale_action) 
scale.pack()

# Checkbutton:
def checkbutton_action():
    print(checked_state.get())  # Prints 1 if on button checked, else 0.
    
# Variable to hold on to checked state, 0 is off and 1 is on.
checked_state = IntVar()        # IntVar is actually a class and the class of this object is stored inside checked_state.
checkbutton = Checkbutton(text = "Is On ?", variable = checked_state, command = checkbutton_action)
checked_state.get()
checkbutton.pack()

# Radiobutton:
def radio_action():
    print(radio_state.get())
    
radio_state = IntVar() # IntVar is actually a class and the class of this object is stored.
radiobutton1 = Radiobutton(text = "Option 1", value = 1, variable = radio_state, command = radio_action)
radiobutton2 = Radiobutton(text = "Option 2", value = 2, variable = radio_state, command = radio_action)
radiobutton1.pack()
radiobutton2.pack()

# Listbox:
def listbox_used():
    print(listbox.get(listbox.curselection()))      # Gets current selection from the listbox.
    
listbox = Listbox(height = 4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for fruit in fruits:
    listbox.insert(fruits.index(fruit), fruit)
    listbox.bind("<<listbox select>>", listbox_used)    # bind function us used to call a particular callback.
    listbox.pack()
    




















window.mainloop()
