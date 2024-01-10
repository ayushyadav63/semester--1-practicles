# List Operations
list1 = [1, 5, 'yadav', 'ayush', '@']

# Search the position of the given element in the list
print(list1.index('yadav'))

# Adding element to a list
list1.append('#')
print(list1)

# Data type
print(type(list1))

# Search the element at a given position
print(list1[2])

# Tuple Operations
# Data type by default
tuple1 = 1, 2, 'yadav', 'ayush', '#'
print(type(tuple1))

# Tuple with single element
tuple2 = 1,
print(type(tuple2))

# Tuple Operations
t = (1, 2, 3, 4, 5)

# Minimum
print(min(t))

# Maximum
print(max(t))

# Count
print(t.count(5))

# Index
print(t.index(5))

# Sum
print(sum(t))

# Adding or updating in tuple is not possible
# t.append('9')  # This line will raise an error

# Dictionary Operations
keys = [1, 2, 3, 4, 5]
values = [1, 2, 'yadav', 'ayush', '#']

# Creating a dictionary using zip
data = dict(zip(keys, values))
print(data)

# Deleting data from dictionary
del data[3]
print(data)

# Searching for a meaning using a keyword
print(data.get(3, "Key not found"))

# String Operations
list1 = [1, 3, "ayush", "yadav", 9]
list2 = ["tata", "bata", 4, 6, 0]

# Add string operator
list3 = list1 + list2
print(list3)

# Multiply string operator
a = list1 * 3
print(a)

# In string operator
if "a" in "ayush":
    print("Found")
else:
    print("Not found")

# Not in string operator
if "a" not in "uyush":
    print("Not found")
else:
    print("Found")


# Function in Python
def calculate(a, b):
    add = a + b
    subtract = a - b
    multiply = a * b
    division = a / b
    modulus = a // b
    remainder = a % b
    print("Addition of numbers is", add)
    print("Subtract of numbers is", subtract)
    print("Multiply of numbers is", multiply)
    print("Division of numbers is", division)
    print("Modulus of numbers is", modulus)
    print("Remainder of numbers is", remainder)


calculate(5, 2)


# Try and Except Use
def divide(a, b):
    try:
        result = a / b
        print("The result of division is", result)
    except Exception as e:
        print("Exception:", e)


divide(5, 2)

# Reversing the word or sentence
user_inp = input("Enter the word: ")
reverse = user_inp[::-1]
print(reverse)

# Program to find numbers that are divisible by 7 but not by 5 and arrange them in a sequence
a = []  # Empty list to arrange the values
min_term = int(input("Enter the min term: "))
max_term = int(input("Enter the max term: "))
for i in range(min_term, max_term):
    if i % 7 == 0 and i % 5 != 0:
        a.append(i)  # Adding the values stored in i to list (a) using append
print(a)

# Class and __init__ method
class Calculate:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def extract_details(self):
        print("The details are as follows:", self.name, self.age)


a = Calculate("ayush", 18)
a.extract_details()

# Constructor in Python is __init__ method
class Hai:
    def __init__(self, name):
        self.name = name

    def say_hai(self):
        print("HAI", self.name)


h = Hai(name=input("Enter your name: "))
h.say_hai()

# Overriding in Python
# Inheriting properties of a parent class to a child class
# Example also for the topic=INHERITANCE

# Python program to demonstrate
# method overriding

# Defining parent class
class Parent:
    # Constructor
    def __init__(self):
        self.value = "Inside Parent"

    # Parent's show method
    def show(self):
        print(self.value)


# Defining child class
class Child(Parent):
    # Constructor
    def __init__(self):
        self.value = "Inside Child"

    # Child's show method
    def show(self):
        print(self.value)


# Driver's code
obj1 = Parent()
obj2 = Child()

obj1.show()
obj2.show()
