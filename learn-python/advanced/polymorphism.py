# Python Polymorphism

# Different classes can use the same method name.


class Dog:

    def sound(self):
        print("Dog says Woof")


class Cat:

    def sound(self):
        print("Cat says Meow")


class Bird:

    def sound(self):
        print("Bird says Tweet")


# Create objects

animals = [Dog(), Cat(), Bird()]


# Use the same method

for animal in animals:
    animal.sound()
