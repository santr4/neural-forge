# OOPs
# Classes and Objects

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def introduce(self):
        print(f"I am {self.name} and I scored {self.marks} marks.")

s1 = Student("Aaranyak", 95)
s1.introduce()

# inheritance

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

dog = Dog()
dog.speak()
dog.bark()

# Encapsulation

class BankAccount:
    def __init__(self, owner, balance, password):
        self.owner = owner
        self._balance = balance  # Internal-use attribute
        self.__password = password  # private attribute

    def get_balance(self, password):
        if password == self.__password:
            return self._balance
        else:
            return "Incorrect password!"

    def deposit(self, amount, password):
        if amount > 0:
            if password == self.__password:
                self._balance += amount
                return f"Deposited {amount}. New balance: {self._balance}"
            else:
                return "Incorrect password!"
        else:
            return "Invalid amount!"

    def withdraw(self, amount, password):
        if password != self.__password:
            return "Incorrect password!"

        if amount <= 0:
            return "Withdrawal must be positive!"

        if amount > self._balance:
            return "Insufficient balance!"

        self._balance -= amount
        return "Withdrawal successful!"

account = BankAccount("Alex", 1000, "abc123")

print(account.owner)
print(account.get_balance("abc123"))

print(account.deposit(500, "abc123"))
print(account.get_balance("abc123"))

print(account.withdraw(200, "abc123"))
print(account.get_balance("abc123"))

# print(account.__password) -> this will give error
print(account._BankAccount__password)  # Accessing private attribute using name mangling

# Polymorphism

class Cat:
    def speak(self):
        return "Meow"

class Dog:
    def speak(self):
        return "Bark"

for animal in [Cat(), Dog()]:
    print(animal.speak())