# Functions and important arguments

def multiply(a, b=2):
    return a * b

print(multiply(5))
print(multiply(5, 3)) # here b is passed as 3, so it will override the default value of b which is 2

print(multiply(b=4, a=5)) # here we are passing the arguments by name, so the order doesn't matter

# *args and **kwargs

# *args -> it collects all the positional arguments into a tuple
# **kwargs -> it collects all the keyword arguments into a dictionary

def show(*args, **kwargs):
    print(args)
    print(kwargs)

show(1, 2, 3, name="Aaranyak", age=23)

# lambda functions

square = lambda x: x**2
print(square(5))