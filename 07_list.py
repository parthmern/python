marks = [95, 96, 97]
print(marks[1]) # 96

print(marks[-1]) # 97 (minus means piche se ginti shuru kar rahe he)
print(marks[-2]) # 96
# print(marks[-5]) # IndexError: list index out of range

print(marks[0:2])   # [95, 96]  0 -> <2 index

for score in marks:
    print(score)

marks.append(99)
print(marks)    # [95, 96, 97, 99]

marks.insert(1, 78) # inser at index
print(marks)  # [95, 78, 96, 97, 99]

print(99 in marks)  # True
print(len(marks))   # 5

i=0
while i< len(marks):
    print(marks[i])
    i+=1

marks.clear()
print(marks)    #[]

marks.pop() # remove last ele
marks.pop(1) # remove ele from specific index

# funcs -------------- ( all in original string )

list = [2, 1, 3]

list.append(4)            # adds one element at the end [2, 1, 3, 4]
list.sort()               # sorts in ascending order [1, 2, 3]
list.sort(reverse=True)   # sorts in descending order [3, 2, 1]
list.reverse()            # reverses list [3, 1, 2]
list.insert(1, 10)        # insert element at index
print("---", list)

ans = list.copy()       # shallow copy
ans[0] ="part"      
print("Original list:", list)   # [1, 10, 2, 3, 4]
print("copied list", ans)   # ['part', 10, 2, 3, 4]

# shallow copy should somehow also change the original, but that’s not true for immutable elements (like int, str)
# Shallow copy only affects nested mutable objects if modified.
# explain

class Person:
    def __init__(self, name):
        self.name = name

p1 = Person("Alice")
p2 = Person("Bob")

lst = [p1, p2]
newlst = lst.copy() # shallow copy so objects reference were stored in string

newlst[0].name = "cool"
for ele in newlst:
    print(ele.name) # cool
