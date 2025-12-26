# set - unique only
marks={1,2,3,4,2,2}
print(marks)    # {1, 2, 3, 4} 

# print(marks[0]) # Not index based -> TypeError: 'set' object is not subscriptable
# so unordered 

for m in marks:
    print(m)
