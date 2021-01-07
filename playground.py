def add(*args):
    result = 0
    for n in args:
        result += n
    return result


print(add(9, 4, 4))


def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    n /= kwargs["divide"]
    print(n)


calculate(2, add=3, multiply=5, divide=2)

class Car:

    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.colour = kwargs.get("colour")

my_car = Car(colour="yellow")
print(my_car.colour)