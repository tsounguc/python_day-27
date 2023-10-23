
# args is a tuple
def add(*args):
    total = 0
    for n in args:
        total += n
    return total


print(add(3, 5, 6))


# kwargs is a dictionary
def calculate(**kwargs):
    print(kwargs)
    # for key in kwargs:
    #     print(key)
    #     print(kwargs[key])
    for (key, value) in kwargs.items():
        print(f"{key}: {value}")
    print(kwargs["add"])


calculate(add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        # self.make = kw["make"]
        # self.model = kw["model"]
        # lines below do the same thing but don't throw an error is one of the attributes weren't set
        self.make = kw.get("make")
        self.model = kw.get("model")


my_car = Car(make="Nissan", model="GT-R")
print(my_car.make)
print(my_car.model)
