# Python Inheritance

# A child class can use code from a parent class.


# Parent class

class Animal:

    def speak(self):
        print("Animal makes a sound")


# Child class

class Dog(Animal):

    def bark(self):
        print("Dog says Woof")


# Create objects

animal = Animal()
dog = Dog()


# Use methods

animal.speak()

dog.speak()
dog.bark()
