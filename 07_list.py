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