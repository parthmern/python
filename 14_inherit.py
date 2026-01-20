# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

    @staticmethod
    def eyes():
        print("2 eyes")


# Child class
class Dog(Animal):  # Inherits from Animal
    def speak(self):
        print(f"{self.name} barks")


dog = Dog("Buddy")
dog.speak()  # Output: Buddy barks
dog.eyes()  # 2 eyes
Animal.eyes() # 2 eyes
