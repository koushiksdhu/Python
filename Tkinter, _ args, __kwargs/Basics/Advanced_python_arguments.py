# Keyword Arguments:
def my_functions(a, b, c):
    pass    # pass keyword is used intentionally because nothing is being implemented inside a function.
    # Do this with a.
    # Do this with b.
    # Do this with c.
    
# Arguments with default values:
def my_function(a = 1, b = 2, c = 3):   # Function is being given with some default values. If formal parameters is not specified than this default value will take on thar.
    pass    # pass keyword is used intentionally because nothing is being implemented inside a function.
    # Do this with a. If a values is passed in the actual parameter. If not passed then keep the default value.
    # Do this with b. If b values is passed in the actual parameter. If not passed then keep the default value.
    # Do this with c. If c values is passed in the actual parameter. If not passed then keep the default value.

s# Example 1:
# Sum the number passed in the actual parameter. If number is not passed then keep the default value = 10 for all that parameters.
def sum(a = 10, b = 10, c = 10):
    print(a + b + c)
sum( a = 1, b = 1, c = 1)   # -> 3
sum(1, 1)   # Only a's and b's value is passed and c's take on that defult value. -> 12
sum(1)  # Only a's value is passed. -> 21   # b's and c's still take on that default value.
sum() # No value is passed. -> 30  default value is added and returned in this case.



