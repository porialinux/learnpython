# Python List Comprehension

# Create a list with a for loop

numbers = []

for number in range(5):
    numbers.append(number)

print(numbers)


# Create a list with list comprehension

numbers = [number for number in range(5)]

print(numbers)


# Create a list of squares

numbers = [1, 2, 3, 4, 5]

squares = [number * number for number in numbers]

print(squares)


# Get even numbers

numbers = [1, 2, 3, 4, 5, 6]

even_numbers = [number for number in numbers if number % 2 == 0]

print(even_numbers)
