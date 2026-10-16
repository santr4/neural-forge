# tuples -> immutable sequences

point = (10, 20)
print(point[0])

x, y = point
print(x)
print(y)

single = (5,)
print(single)

# One thing is that tuples are immutable, but lists inside them can be changed.

t = (1, 2, [30, 40])
t[2].append(80)
print(t)