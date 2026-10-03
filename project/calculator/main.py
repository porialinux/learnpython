# Basic Calculator

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b


num1 = int(input("First number: "))
num2 = int(input("Second number: "))

print("Sum:", add(num1, num2))
print("Minus:", subtract(num1, num2))
print("Multiply:", multiply(num1, num2))
print("Divide:", divide(num1, num2))
