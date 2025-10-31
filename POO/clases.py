# Defining a class

class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
        
    def __str__(self):
        return f"Dog {self.name} breed {self.breed} and {self.age} years old"
    
    # Create a dog

    dog1 = Dog("Nemesis","Corgi",3)