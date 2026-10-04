# Python Function Arguments


# 1. Normal arguments

def greet(name):
    print("Hello", name)


greet("Poria")


# 2. Multiple arguments

def add(a, b):
    print(a + b)


add(5, 3)


# 3. Default arguments

def welcome(name="Guest"):
    print("Welcome", name)


welcome()
welcome("Poria")


# 4. Keyword arguments

def info(name, age):
    print("Name:", name)
    print("Age:", age)


info(age=16, name="Poria")
