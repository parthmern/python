# list you can add,del mutable things but in tuple we cannot do
# tuple → immutable

marks=(1,2,3,4,3)

print(marks.count(3))   # 2 
print(marks.index(3))   # 2

person = "a", "bb", "cc"    # syntax change
print(person.index("bb"))   # 1