def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


def calc(a, b, operation):      # This is called higher order functions.
    print(operation(a, b))


calc(5, 7, add)
calc(7, 5, sub)
calc(5, 4, mul)
calc(40, 10, div)

# Python functions are first class objects, and can be passed around as arguments. E.g., int/string/float etc.

# Nested Functions: Functions can also be nested inside other functions.


def outer_function():
    print('I am outer function')

    def nested_function():      # This function is only accesible by the outer_function.
        print('I am nested function')

    # This function is only accesible inside the outer_function only.
    nested_function()

# If we call the nested function then we'll get a name error. This is undefined because that function is nested inside an outer_function.
# We can call that nested_function inside outer_function only.


outer_function()  # calling the outer_function.


# Functions can be returned from another functions.
def outer_function_copy():
    print("This is outer function copy.")

    def inner_function_copy():
        print("This is inner function copy")

    return inner_function_copy


inner_function_copy = outer_function_copy()

# Calling the inner_funtion that is being returned by the outer_function.
inner_function_copy()
