# Defining a class

class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
        
    def __str__(self):
        return f"Dog {self.name}, breed {self.breed} and {self.age} years old"
    
    #Method

    def bark (self):
        print(f"{self.name} is barking")

    def play (self, toy):
        print(f"{self.name} is playing with the {toy}")


# Create a dog

dog1 = Dog("Nemesis","Corgi",3)

print(dog1)

print(f"Nombre del cachorro: {dog1.name}")

dog1.bark()

dog1.play("bone")