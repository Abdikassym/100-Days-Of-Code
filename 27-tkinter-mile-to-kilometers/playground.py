# Unlimited Positional Arguments
def add(*args):
    print(args[1])
    total = 0
    for i in args:
        total += i
    print(total)


# add(1, 2, 3, 4, 5)


# Keyword Arguments
def calculate(n, **kwargs):
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


# calculate(4, add=3, multiply=2)


class Car:
    def __init__(self, **kw):
        self.model = kw.get("model")
        self.make = kw.get("make")


car = Car(model="Toyota")
print(car.make)
