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

# map, filter, zip, enumerate

n = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, n))
evens = list(filter(lambda x: x % 2 == 0, n))
print(squares)
print(evens)

# Added the below examples for zip and enumerate functions using Gemini 3.6 Flash Agent

# zip() -> combines multiple iterables (e.g., lists, tuples) element-wise into tuples
# It stops when the shortest input iterable is exhausted
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

# zip combines corresponding elements from names and scores
combined = list(zip(names, scores))
print(combined)  # Output: [('Alice', 85), ('Bob', 92), ('Charlie', 78)]

# Iterating over multiple lists simultaneously using zip
for name, score in zip(names, scores):
    print(f"{name}: {score}")


# enumerate() -> adds an automatic index/counter to an iterable and yields pairs of (index, item)
fruits = ["apple", "banana", "cherry"]

# By default, indexing starts at 0
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

# You can also set a custom start index (e.g., start=1)
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")

# Loops, conditions, and Exceptions

for i in range(5):
    print(i)

score = 75

if score > 75:
    print("You passed with distinction!")
elif score >= 50:
    print("You passed!")
else:
    print("You failed!")