def outer_function():
    print("I'am outer function")

    def nested_function():
        print("I'am nested function")

    return nested_function


inner_function = outer_function()
inner_function()
