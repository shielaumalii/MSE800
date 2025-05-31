# Parent class
class Animal:
    def speak(self):
        return "The animal makes a sound"

# Child class inheriting from Animal
class Dog(Animal):
    def bark(self):
        return "The dog barks"

# Create an instance of Dog
my_dog = Dog()

# Call methods from both parent and child classes
print(my_dog.speak())  # Inherited from Animal
print(my_dog.bark())   # Defined in Dog
