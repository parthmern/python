class Student:
    
    college = "ABC College"   # public class variable
    _branch = "CSE"           # protected variable (convention)
    __fees = 50000            # private variable (name mangling)

    def show(self):
        print(self.college)   # public access
        print(self._branch)   # protected access
        print(self.__fees)    # private access inside class
        self.__hello()

    def __hello(self):
        print("i am private method")


s = Student()

print(s.college)             # public → allowed
print(s._branch)             # protected → allowed (but not recommended)

# print(s.__fees)            # ❌ error (private)
print(s._Student__fees)      # ✅ private accessed using name mangling
# s.__hello() # AttributeError private

s.show()

