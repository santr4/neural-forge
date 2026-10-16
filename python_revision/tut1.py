# Lists -> mutable sequences of items

n = [10, 20, 30, 40]

# print(n[0])
# print(n[-1])
# print(n[1:3])

n.append(50)
n.insert(1, 15) # at index 1, insert 15
n.remove(30) # removes the first occurrence of 30
n.pop() # removes the last item

# print(len(n))
# print(n)

list1 = [4, 2, 8, 1, 2]

list1.sort()
list1.reverse()

print(list1)
print(list1.count(2)) # counts the number of occurrences of 2
print(8 in list1) # checks if 8 is in the list

squares = [x**2 for x in range(1, 6)]
print(squares)

