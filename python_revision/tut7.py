# super() in python

class A:
    def __init__(self):
        print("I am the parent class")

class B(A):
    def __init__(self):
        super().__init__()
        print("I am the child class")

b = B()

# decorators in python


def calculate_square_cube(func):
    def wrapper(*args, **kwargs):
        num = func(*args, **kwargs)
        square = num ** 2
        cube = num ** 3
        print(f"Number: {num}")
        print(f"Square: {square}")
        print(f"Cube: {cube}")
        return num
    return wrapper

# decorator function
@calculate_square_cube
def input_number(a):
    return a


input_number(5)