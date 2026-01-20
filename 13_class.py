class Person:
    def __init__(self, name, age):
        self.name = name   # attribute
        self.age = age     # attribute

    def greet(self):
        return f"Hello, my name is {self.name}"

p1 = Person("Parth", 22)

print(p1.name)      # Parth
print(p1.greet())   # Hello, my name is Parth

# Static Methods
# Methods that do NOT use the 'self' parameter
# They work at the CLASS level, not on object data
class Student:
    
    @staticmethod       # dacorator
    def college():
        print("ABC College")

Student.college() 