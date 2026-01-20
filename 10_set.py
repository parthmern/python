# set - unique only
marks={1,2,3,4,2,2}
print(marks)    # {1, 2, 3, 4} 

# print(marks[0]) # Not index based -> TypeError: 'set' object is not subscriptable
# so unordered 

for m in marks:
    print(m)

# funcs

null_set = set( ) #empty set syntax

s1 = {1, 2, 3}
s2 = {3, 4, 5}

s1.add(6)                     # adds 6 → {1, 2, 3, 6}
s1.remove(1)                  # removes 1 → {2, 3, 6}
s1.pop()                       # removes a random element → e.g., {3, 6}
s1.clear()                     # empties s1 → set()
s1 = {2, 3, 6}                 # reset s1 for union/intersection examples
s1.union(s2)                   # union → {2, 3, 4, 5, 6}
s1.intersection(s2)            # intersection → {3}
