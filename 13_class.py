class Person:
    def __init__(self, name, age):
        self.name = name   # attribute
        self.age = age     # attribute

    def greet(self):
        return f"Hello, my name is {self.name}"

p1 = Person("Parth", 22)

print(p1.name)      # Parth
print(p1.greet())   # Hello, my name is Parth
