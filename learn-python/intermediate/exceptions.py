# Python Exceptions

# An exception is an error in a program.
# We can use try and except to handle errors.


# Simple try and except

try:
    number = int(input("Enter a number: "))
    print(number)

except:
    print("Please enter a number")


# Handle a specific error

try:
    number = int(input("Enter a number: "))
    result = 10 / number

    print(result)

except ValueError:
    print("Please enter a number")

except ZeroDivisionError:
    print("You cannot divide by zero")


# Try, except and else

try:
    number = int(input("Enter a number: "))

except ValueError:
    print("Please enter a number")

else:
    print("Your number is", number)
