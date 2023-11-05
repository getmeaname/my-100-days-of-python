def add(*args):
    Total = 0
    for n in args:
        Total += n
    return Total


print(add(3, 4, 6, 7))


def calculate(n, **kw):
    print(kw)
    for (key, value) in kw.items():
        print(key)
        print(value)
    n += kw["add"]
    n *= kw["mul"]
    print(n)


calculate(2, add=20, mul=30)


class Car:

    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.color = kw.get("seats")


my_car = Car(make="Honda")  # Add or leave the default values which is none.
print(my_car.model)
