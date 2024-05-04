# 1. Creating a Python Decorator Function
import time


def delay_function(function):
    def wrapper_function():
        print("Start of function")
        function()
        print("Second use of function")
        function()
        print("End of the function")
    return wrapper_function


@delay_function
def say_hello():
    print("Hello!")


def say_bye():
    print("Bye!")


def say_wassup():
    print("Wassup!")


dec_func = delay_function(say_hello)
dec_func()
