# Strings and slicing

t = "Deep Learning"

print(t[0])
print(t[-1])
print(t[0:4]) # slicing from index 0 to 3
print(t[::-1])

print(t.lower())
print(t.upper())
print(t.split())

# formatting strings

name = "Aaranyak"
score = 100

s = f"Hello, I am {name} and my score is {score}"
print(s)