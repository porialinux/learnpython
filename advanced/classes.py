# Python Classes

# __init__ runs when we create a new object.
# It sets the first values of the object.


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age


    def show_info(self):
        print("Name:", self.name)
        print("Age:", self.age)


# Create objects

person1 = Person("Poria", 16)
person2 = Person("Ali", 17)


# Show object information

person1.show_info()
person2.show_info()
