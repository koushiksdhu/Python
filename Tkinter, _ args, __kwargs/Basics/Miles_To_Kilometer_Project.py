from tkinter import *

window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width = 250, height = 100)
window.config(padx = 40, pady = 20)

# ENTRY
entry = Entry(width = 8)
entry.grid(row = 0, column = 1)

# LABEL:
miles = Label(text = "Miles")
miles.grid(row = 0, column = 2)

is_equal = Label(text = "is equal to ")
is_equal.grid(row = 2, column = 0)

ans = Label(text = "")
ans.grid(row = 2, column = 1)

km = Label(text = "KM.")
km.grid(row = 2, column = 2)

# BUTTON ACTION:
def button_action():
    value = round(float(entry.get()) * 1.609)
    # ans["text"] = value
    # OR
    ans.config(text = value)

# BUTTON:
button  = Button(text = "Calculate", command = button_action)
button.grid(row = 3, column = 1)


window.mainloop()