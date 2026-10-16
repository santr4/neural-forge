# sets -> it only contains unique elements

a = {1, 2, 2, 2, 3, 5}
print(a)

b = {3, 4, 5}
print(a | b) # union
print(a & b) # intersection
print(a - b) # difference

a.add(10)
a.discard(2)
print(a)

users = ["alice", "bob", "alice", "sam"]
unique_users = list(set(users))
print(unique_users)

# dictionaries -> key-value pairs

student = {
    "name": "Aaranyak",
    "age": 23,
    "score": 85
}
# print(student["name"])
student["score"] = 92
student["city"] = "Raipur"
del student["age"]

for key, value in student.items():
    print(key, value)