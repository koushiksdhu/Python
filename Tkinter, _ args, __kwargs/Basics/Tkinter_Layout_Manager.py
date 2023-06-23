from tkinter import *

window = Tk()
window.title("My First GUI Programs")
window.minsize(height = 500, width = 500)
window.config(padx = 40, pady = 40)     # Adding Padding to all the edge of the window. [padx = Padding at x axis and pady = Padding at y axis]

# LABEL:
label = Label(text = "This is a Label.", font = ("Times New Roman", 15, "bold"))
# label.pack()  
# You cannot mix up pack() and grid() in the same program. If you do these, then error will be thrown. Basically, this two are incomoatible with each other. Rather, we have choose among them the one.
label.grid(row = 0, column = 0)         # Using grid() layout manager.

# BUTTON:
def button_clicked():
    label["text"] = "Button got clicked."
    
new_button = Button(text = "New Button", command = button_clicked)
# button.pack()
new_button.grid(row = 0, column = 2)        # Using grid() layout manager.

button = Button(text = "Button", command = button_clicked)
button.grid(row = 1, column = 1)


# ENTRY:
entry = Entry(width = 10)
print(entry.get())
# entry.pack()
# entry.pack(side = "left")      # It will move towards the left center position or left edge of the program.
# In pack(), to place the widget in a particular position, then it is very very complicated to do so.

# entry.place(x = 0, y = 0)   # to place in a particular x and y coordinates using place() method. It will place the entry to the top left corner i.e., x = 0 and y = 0 position.
entry.grid(row = 2, column = 3)     # Using grid() layout manager.



# TKINTER LAYOUT MANAGERS: Tkinter has many layout managers which is used to define how to position each of the widgets in your program.
# There are mainly three layout managers: Pack(), Place(), and Grid().

# Pack(): It pack each of the widgets next to each other in a variabluy logically format and by default, pack will always start from the top and pack the evry other widget just below the previous one.

# Place(): Place is all about precise positioning. so, when you place something, then you can provide x and y coordinates values.

# If any widgets is created an is not specified using any of the three method (i.e., pack(), place(), or grid()) then it would not be displayed on the screen/window.

# Grid(): Just imagine, your whole program is a grid and it is being divided in a row and column major (Rows in horizontal and column which go along the vertical)
# In grid, column and row number is passed to place the widget in a particular position.

window.mainloop()