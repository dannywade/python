class Dog:
    """A simple class to model a dog"""

    def __init__(self, name, age):
        """Initialize name and age attributes"""
        self.name = name
        self.age = age
    
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over! ")

# Creating an instance of the Dog class
my_dog = Dog('Wille', 6)

# Accessing an attribute
print(my_dog.name)

# Calling on a class method
my_dog.sit()