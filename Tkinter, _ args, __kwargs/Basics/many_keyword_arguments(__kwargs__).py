# kwargs means Keyword Arguments.
# **kwargs means Unlimited Keyword Arguments.
# kwargs is basically a dictionary.

def calculate(n, **kwargs):
    print(kwargs)   
    print(type(kwargs))     # dictionary.
    for(key, value) in kwargs.items():
        print(key, value)   # Both key and value will get printed.
        print(key)          # Only key will get printed.
        print(value)        # Only value will get printed.
        
        print(kwargs["add"])    # the value of the key will get printed.
        
        n += kwargs["add"]          # The value of the key is added to n.
        n *= kwargs["multiply"]     # The value of the key is multiplied by n.
        print(n)

# When keywords are used the order of the arguments listed does not matter. Python matches by name not position.
calculate(n = 2, add = 4, multiply = 10)  # Unlimited (key, value) pair is passed.

# Example of arg, *args and **kwargs:
def all_aboard(a, *args, **kw): 
    print(a, args, kw)

all_aboard(4, 7, 3, 0, x=10, y=64)      # 4 is passed by position. 7,3,0 are collected into a tuple. x and y are in a keyword dictionary..

# Three methods:

# At object creation time, using keyword arguments:
# fred = Button(self, fg = "red", bg = "blue")

# After onjecvt creation, traeting the option name like dictionary object:
# fred["fg"] = "red"
# fred["bg"] = "blue"

# Use the config() method to update multiple attributes subsequent to object creation:
# fred.config(fg = "red", bg = "blue")

# For more information head towards Tcl/Tk documentation.
