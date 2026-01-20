# list you can add,del mutable things but in tuple we cannot do
# tuple → immutable

marks=(1,2,3,4,3)

print(type(marks)) # <class 'tuple'>

print(marks.count(3))   # 2 
print(marks.index(3))   # 2

person = "a", "bb", "cc"    # syntax change
print(person.index("bb"))   # 1

# init tuple with one ele
tup = (1)
print(type(tup))    # <class 'int'>
tup = (1,)          # fix inti with , in end
print(type(tup))    # <class 'tuple'>