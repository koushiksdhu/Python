# Python Decorators
import time


def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        # Do something before
        function()
        function()  # Will run it twice.
        # Do something after
    # Function should be returned without parentheses.
    return wrapper_function


@delay_decorator
def say_hello():
    print("Hello")


@delay_decorator
def say_bye():
    print("Bye")


def greeting():
    print("How are you ?")


say_hello()         # This  will delay the call for 2s then print it twice.
greeting()          # This will not delay the call and directly print.


# Other way to use a decorator function:
decorated_function = delay_decorator(greeting)
decorated_function()
# @delay_decorator does the same work as above. It is just the decorated version of the above one.
