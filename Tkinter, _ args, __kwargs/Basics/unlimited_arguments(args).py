# *args -> Inside any function, If *args is passed as a parameter than than function can take any number of arguments.
# This is known as Unlimited Arguments or Unlimited Positional Arguments.
# Find the sum of all the elements that are passed in an actual parameter during function call
# In this case, we'll use *args in formal parameter.

def sum(*args):     # * means any numbers of arguments or unspecified number of arguments. We can also use any other name in place of args.
    sum = 0
    print(args)         # If we just print args then it return or print a tuple. 
    print(type(args))   # Doing typecheck.
    for i in args:      # Iterating over the tuple named as args.
        sum += i
    return sum

# You can pass as many arguments as you want.
print("Sum:",sum(1, 2, 3, 4))
print("Sum:",sum(10, 20, 30, 40, 50, 60))
print("Sum:",sum(10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10))
print("Sum:",sum(4))